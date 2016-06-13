import bottle
from bottle import route
from bottle import post
from bottle import request
from bottle import error
from bottle import debug
from jinja2 import Environment, FileSystemLoader
import logging
import json
from os.path import dirname
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import taskqueue
from google.appengine.api import urlfetch
from payments import stripe_pay
from models import Account

JINJA_ENV = Environment(
    loader=FileSystemLoader(dirname(__file__) + '/templates/'),
    extensions=['jinja2.ext.autoescape'])


@route('/')
@post('/')
def home():
    user = users.get_current_user()
    login_url = users.create_login_url(request.path)
    if not user:
        return respond('home.html', {'login_url': login_url, 'user': user})
    account = None
    warn_msg = None
    success_msg = None
    account = Account.get_or_insert(user.user_id(), user_id=user.user_id())
    if not account.email:  # ensure this is set on account creation
        account.email = user.email()
    if request.forms.get('update_sites'):
        site_urls = [
            request.forms.get(
                'site' + str(i)) for i in range(1, 6) if request.forms.get(
                'site' + str(i)
            )
        ]
        account.sites = site_urls
        account.put()
    elif request.forms.get('stripeToken'):
        if account.upgraded:
            logging.info(
                "User {} attempted to pay for an already-paid account".format(
                    user.email()
                )
            )
            warn_msg = "This account appears to have already paid"
        else:
            charge, msg = stripe_pay(
                500,
                request.forms.get('stripeToken'),
                user
            )
            if charge is not None:
                success_msg = msg
                chargejson = {
                    'method': 'Stripe',
                    'id': charge.id,
                    'created': charge.created,
                    'amount': charge.amount,
                    'type': charge.card.type,
                    'balance_transaction': charge.balance_transaction,
                    'description': charge.description
                }
                account.payment_info = json.dumps(chargejson)
                account.upgraded = True
                account.put()
            else:
                warn_msg = msg
    return respond(
        'home.html',
        {
            'login_url': login_url,
            'user': user,
            'account': account,
            'warn_msg': warn_msg,
            'success_msg': success_msg
        }
    )


def respond(template_file, params):
    tpl = JINJA_ENV.get_template(template_file)
    return tpl.render(**params)

@route('/cron/site_checks')
def site_checks():
    account_query = Account.query()
    for account in account_query.iter():
        taskqueue.add(
            url='/queue/site_check/{}'.format(account.user_id),
            params={},
            method="GET"
        )


@route('/queue/site_check/<user_id>')
def site_check(user_id):
    account = Account.get_by_id(user_id)
    failed_site_reports = []
    for site in account.sites:
        if site:
            result = urlfetch.fetch(site)
            if result.status_code != 200:
                failed_site_reports.append(
                    "site {} failed with a {} status code".format(
                        site,
                        result.status_code
                    )
                )
    if failed_site_reports:
        failed_site_report = '\n'.join(failed_site_reports)
        message = mail.EmailMessage()
        message.sender = 'failures@gae_starter@appspotmail.com'
        message.body = """Failures for your site on {}:
        {}
        """.format('downtime-toy.appspot.com', failed_site_report)
        message.subject = "Notification of site failures"
        message.to = account.email
        try:
            message.send()
            logging.info(
                "sent email to {} for failed sites.".format(account.email)
            )
        except:
            logging.warn(
                "failed to send owner email to {} for failed sites.".format(
                    account.email
                )
            )
    else:
        logging.info("no failed sites for email {}".format(account.email))


@route('/admin')
def admin_page():
    if users.is_current_user_admin():
        return respond('404.html', {})
    accounts = Account.query().fetch(limit=100)
    return respond('admin.html', {'accounts': accounts})


def main():
    debug(True)
    app = bottle.app()
    # SESSIONS
    # session_opts = {
    #     'session.type': 'ext:google'
    # }
    # app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)
    # APPSTATS
    #  from google.appengine.ext.appstats import recording
    #  app = recording.appstats_wsgi_middleware(app)
    run_wsgi_app(app)

@error(403)
def error403(code):
    return respond('403.html', {code})

@error(404)
def error404(code):
    return respond('404.html', {code})

if __name__ == "__main__":
    main()
