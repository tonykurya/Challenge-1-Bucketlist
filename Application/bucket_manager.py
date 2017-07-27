# Bucketlist Data Class


class BucketManager(object):
    """
    Define a Operations.

    """

    def __init__(self, bucket, body, _id):
        self.bucket = []
        self.main_bucket = {}
        self._id = _id

    def add_event(self, event):
        self.bucket.append({self._id: event})

    def delete_event(self, key):
        for entry in self.bucket:
            for k, v in entry:
                if key == k:
                    self.bucket.remove(entry)

    def edit_event(self, key, data):
        for entry in self.bucket:
            for k, v in entry:
                if key == k:
                    entry[k] = data

    def add_bucketlist_to_holder(self, bucketlist_name):
        self.main_bucket[bucketlist_name] = {}

    def delete_bucketlist(self, bucketlist_name):
        del self.main_bucket[bucketlist_name]


class User(object):
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def repr(self):
        return(self.email, self.password)
