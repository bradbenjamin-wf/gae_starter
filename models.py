from google.appengine.ext import ndb
import decimal, json
import time, logging

class Account(ndb.Model):
    user_id = ndb.StringProperty()
    email = ndb.StringProperty()
    sites = ndb.StringProperty(repeated=True)
    upgraded = ndb.BooleanProperty(default=False)
    payment_info = ndb.TextProperty()
    def get_sites(self):
    	""" ensures a list of at least 5 sites even if they are empty """
    	while len(self.sites) < 5:
    		self.sites.append('')
    	return self.sites
