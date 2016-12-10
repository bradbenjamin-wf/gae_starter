import json
from google.appengine.ext import ndb


class SillyData(ndb.Model):
    user_id = ndb.StringProperty()
    email = ndb.StringProperty()
    # json is often more useful than modeling multiple NDB objects
    # when you don't need to query on fields in those objects
    raw_data = ndb.JsonProperty()
    
    def raw_data_as_json_str(self):
        if self.raw_data:
            return json.dumps(self.raw_data)
        return json.dumps({})


def get_silly_data(user_id):
    silly_data = SillyData.query(SillyData.user_id == user_id).get()
    if not silly_data:
        # create one
        silly_data = SillyData(user_id=user_id, email=None)
    return silly_data
