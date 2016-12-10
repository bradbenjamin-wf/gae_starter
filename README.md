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

Deploying
============
1. You'll need to create a project at https://console.developers.google.com (ex: project_id: abcde-12345)
2. Change app.yaml application to abcde-12345
3. Run `python appcfg.py update app.yaml` (you'll have to set path to python and appcfg.py if they aren't sym-linked already)
4. Visit https://console.cloud.google.com/appengine?project=abcde-12345 to make sure the version you uploaded is the default version.

Requirements
============
If you need to add dev dependencies, add them to requirements-dev.txt
install dev dependencies using `pip install -r requirements-dev.txt`

If you need to add runtime dependencies, add them to requirements.txt
install runtime dependencies using `pip install -r requirements.txt -t lib/`

Contribution Guidelines
=======
1. Use Github to open pull requests for review.
2. ensure code passes flake8 first
