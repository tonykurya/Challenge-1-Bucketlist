# Bucketlist Data Class


class User(object):
    """
    Define a user.

    """

    def __init__(self, email, password, username, user_data={}):
        self.user_data = user_data
        self.email = email
        self.password = password
        self.username = username

    # Register
    # @classmethod
    def register(self):
        if len(self.email) < 0 or len(self.email) < 6:
            return 'Invalid email'
        elif len(self.username) < 0 or len(self.email) < 6:
            return 'Username must have at least 6 characters'
        elif len(self.password) < 6:
            return 'Password must be at least 6 characters'
        self.user_data[self.email] = {'username': self.username, 'password': self.password}
        return self.user_data
