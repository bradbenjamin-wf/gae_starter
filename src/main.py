
# if you add a dependency to to requirements.txt, you need these 2 lines
# before you use those dependencies, see lib/README.md
from google.appengine.ext import vendor
vendor.add('lib')

import bottle
import json
from bottle import route, post, template, error, request, response
from models import get_silly_data
from core import respond
from google.appengine.ext.webapp.util import run_wsgi_app


@route('/')
def index():
    # example_data is to show how to use params in index.html jinja2 template
    example_data = {'key1': 'keykey1', 'value2': 'valval2',
                    'list': ['something3', 'something4', 'something5']}
    return respond('index.html', params={'data': example_data})


@route('/hardcodedjson/1')
def hardcoded_json_1():
    example_data = {'key1': 'keykey1', 'value2': 'valval2',
                    'list': ['something3', 'something4', 'something5']}
    response.content_type = 'application/json'
    return json.dumps(example_data)


@route('/getuserdata/<user_id>')
def getuserdata(user_id):
    user_data = get_silly_data(user_id)
    response.content_type = 'application/json'
    return user_data.raw_data_as_json_str()


@post('/postuserdata/<user_id>')
def postuserdata(user_id):
    posted_data = request.forms.get('posted_data')
    try:
        parsed_data = json.loads(posted_data)
    except ValueError:
        response.status = 500
        return 'Error parsing JSON post data'

    user_data = get_silly_data(user_id)
    user_data.raw_data = parsed_data
    user_data.put()
    return 'OK'


bottle.debug(True)
# session_opts = {
#     'session.type': 'ext:google'
# }
# app = beaker.middleware.SessionMiddleware(app, session_opts)
# from google.appengine.ext.appstats import recording
# app = recording.appstats_wsgi_middleware(app)
app = bottle.app()


@error(403)
def error403(code):
    return respond('403.html')

@error(404)
def error404(code):
    return respond('404.html')
