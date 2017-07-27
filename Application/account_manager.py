# Bucketlist Data Class


class Bucketlists(object):
    """
    Define a Bucketlist.

    """
    bucketlist_holder = {}
    
    def __init__(self):
        self.bucketlist_name = ""
        self.event = ""
        self.bucketlist_holder = {}
        self.count = 0

    def add_event(self, event):
        self.bucket_list.append({"_id": self.count, 'event': event})
        self.count += 1

    def delete_event(self, _id):
        for event in self.bucket_list:
            if _id == event[_id]:
                self.bucketlist.remove(event)

    def edit_event(self, event):
        pass

    def add_bucketlist_to_holder(self, bucketlist_name):
        self.bucketlist_holder[bucketlist_name] = []

    def delete_bucketlist(self, bucketlist_name):
        del self.bucketlist_holder[bucketlist_name]
