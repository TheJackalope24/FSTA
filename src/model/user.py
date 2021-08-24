from json import JSONEncoder

class User:
    def __init__(self, username, password, apikey):
        self._username = username
        self._password = password
        self._apikey = apikey

    def get_username(self):
        return(self._username)

    def get_password(self):
        return(self._password)

    def get_apikey(self):
        return(self._apikey)


class UserEncoder(JSONEncoder):
    # In order to define how your type should be serialized, you should override the "default"
    # method:
    def default(self, user):
        if isinstance(user, User):
            return user.__dict__
