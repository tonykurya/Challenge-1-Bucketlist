# Bucketlist Data Class
class BucketClass(object):
    """
    Define a Operations.

    """

    def __init__(self, bucket_name, _id, events=[]):
        self.bucket_name = bucket_name
        self._id = _id
        self.events = events

    def add_event(self, _id, description):
        self.events.append({_id: description})

    def delete_event(self, _id):
        for entry in self.events:
            for key in entry.keys():
                if key == _id:
                    self.events.remove(entry)

    def edit_event(self, _id, data):
        for entry in self.events:
            for key in entry.keys():
                if key == _id:
                    entry[key] = data


class User(object):
    def __init__(self):
        self.email = ""
        self.username = ""
        self.password = ""

    def repr(self):
        return(self.email, self.password)
