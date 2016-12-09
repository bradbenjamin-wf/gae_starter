import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/../static/template"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def respond(templateFile, params=None):
    if params is None:
        params = {}
    tmpl = JINJA_ENVIRONMENT.get_template(templateFile)
    return tmpl.render(params)
