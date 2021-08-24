import sqlite3
from src.model.user import User

def add_user(username:str, password:str, apikey:str) -> bool:
    con = sqlite3.connect('stocks.db')
    cur = con.cursor() 
    cur.execute('''INSERT INTO user (username, password, apikey) VALUES (?,?,?)''', (username, password, apikey))
    con.commit()
    con.close()
    return({"success":"true"})

def get_user_by_username(username:str):
    con = sqlite3.connect('stocks.db')
    cur = con.cursor()
    cur.execute('''SELECT username, password, apikey FROM user WHERE username = ?''', (username,))
    rows = cur.fetchone()
    con.close()
    if(rows != None):
        return(User(rows[0],rows[1],rows[2]))

