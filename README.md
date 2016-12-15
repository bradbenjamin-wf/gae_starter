gae_starter
===========

This is a simple GAE starter to show how easy it is to get a server running on App Engine, so you can focus on client-side aspects of your project.

If you need to just have a server return some hard-coded JSON and work on a real server response later, this is a good starter.
If you need to save some simple data, you're better off using this than setting up a database and a server and all of that.  This is way easier.
If you want a simple web application, this is a good starter as I've built over 10 sites using this basic framework.

It uses these basic technologies:

1. [GAE](https://developers.google.com/appengine/)
2. [bottle.py](http://bottlepy.org/) for handling requests, these are the @route annotations for assigning URL's to handler methods
3. [jinja2](http://jinja.pocoo.org/docs/dev/) for HTML templating in static/template/ folder

If you want to go further and add payments, cron jobs, or task queues, you may want to check out the older `full_example` branch.

Setup for Windows
============
1. Install Python 2.7: https://www.python.org/downloads/ 
2. Install App Engine SDK for Python https://storage.googleapis.com/appengine-sdks/featured/GoogleAppEngine-1.9.40.msi
3. Open GoogleAppEngineLauncher and add gae_starter as a project ('gae_starter' app name, /path/to/workspace/ as folder)

Setup for Mac
============
1. Install Python 2.7 https://www.python.org/downloads/release/python-2713rc1/
2. Install App Engine SDK for Python https://storage.googleapis.com/appengine-sdks/featured/GoogleAppEngineLauncher-1.9.49.dmg
3. Open GoogleAppEngineLauncher and add gae_starter as a project ('gae_starter' app name, /path/to/workspace/ as folder)

Requirements
============
If you need to add dev dependencies, add them to requirements-dev.txt
install dev dependencies using `pip install -r requirements-dev.txt`

If you need to add runtime dependencies, add them to requirements.txt
install runtime dependencies using `pip install -r requirements.txt -t lib/`

Running Locally
============
Running locally is as simple as pressing Run in GoogleAppEngine launcher after selecting your project, then hitting
 Browse to visit the localhost URL.  When developing
 a client app, such as Android/iOS, you may find it useful to run against your localhost service. 

Deploying
============
1. You'll need to create a project at https://console.developers.google.com (ex: project_id: abcde-12345)
2. Change app.yaml application to abcde-12345
3. Run `python appcfg.py update app.yaml` (you'll have to set path to python and appcfg.py if they aren't sym-linked already)
4. Visit https://console.cloud.google.com/appengine?project=abcde-12345 to make sure the version you uploaded is the default version.

Examples
=======
Examples are very minimal, because I don't want you to have to remove many things to use it.  They are in main.py:
1. `def index():` shows a python dictionary data structure being rendered by static/template/index.html using jinja2.
2. `def hardcoded_json_1():` shows how for prototyping client code, you wouldn't really have to write actual server code
 for quite a while.  You could hard-code responses that you needed, deploy to app engine and not think about server until later.
 This example uses JSON, but you could use plain text, CSV, XML, etc.
3. `def getuserdata(user_id):` shows the use of Google Datastore models for storage, lookup.  The example returns some json on
 the stored entity.  There is no HTML page, it's just showing server providing something, such as to an Android app that hits the URL.
4. `def postuserdata(user_id):` shows the ability to write to the Google Datastore model in example 3.  It takes a HTTP POST parameter named
 "posted_data" which must be valid JSON.

Hopefully with these examples, you can see how to adapt this starter to your own use case.  App Engine documentation is pretty good.
Also, it's a mature project so it has many answers on Stack Overflow also.

Using jinja2 templates
=======
Docs for jinja2 can be found at http://jinja.pocoo.org/docs/dev/
This project sets up a base.html which will be the structure of every page.  Then in index.html it includes base.html and it gets
that structure for free.  You don't want to duplicate your basic HTML structure, menu, and bootstrap styles in many html files, so the
include takes care of that.
It defines blocks like `{% block title %}Default{% endblock %}` with the idea that in index.html you would re-define that block and over-write
the base content.  The base template defines 4 blocks, title, extrastyle, body, and extrascripts.  Extra means optional, so for each page you
can choose only to set title and body.    

Jinja2 is great because you can avoid writing HTML in code.
 You write code to collect variables, and when you need to use them in HTML,
 you enter a code-like tools like for-loops and if-statements in template blocks.

Contribution Guidelines
=======
1. Use Github to open pull requests for review.
2. ensure code passes flake8 first
