from src.database import user_dao


def register(data):
    return(user_dao.add_user(data["username"], data["password"], data["apikey"]))

def login(data):
    user = user_dao.get_user_by_username(data["username"])
    if(data["username"] == user.get_username() and data["password"] == user.get_password()):
        return({"login":"valid"})
    else:
        return({"login":"invalid"})
    