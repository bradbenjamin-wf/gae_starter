import bottle
from bottle import route, template, error, response
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import vendor
vendor.add('lib')

from core import respond


@route('/')
def index():
    # example_data is to show how to use params in index.html jinja2 template
    example_data = {'key1': 'keykey1', 'value2': 'valval2',
                    'list': ['something3', 'something4', 'something5']}
    return respond('index.html', params={'data': example_data})


@route('hardcodedjson/1')
def hardcoded_json_1():
    example_data = {'key1': 'keykey1', 'value2': 'valval2',
                    'list': ['something3', 'something4', 'something5']}
    response.content_type = 'application/json'
    return json.dumps(example_data)


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
    return respond('403.html', {code})

@error(404)
def error404(code):
    return respond('404.html', {code})
