"""This is a home-rolled class to simplify usage of jinja2 templates.  
 You should be able to follow the example templates in /static/templates and their use in main.py,
 and never have to touch this class"""
import os
import jinja2

# This constant references the /static/template folder from the path that core.py lives in.
# (.. to go back 1 folder) 
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/../static/template"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def respond(template_file, params=None):
    if params is None:
        params = {}
    # params can be a good place to automatically inject GAE's login/logout variables
    # or user/session variables.
    tmpl = JINJA_ENVIRONMENT.get_template(template_file)
    return tmpl.render(params)
