import sqlite3

con = sqlite3.connect('stocks.db')

cur = con.cursor()
cur.execute('''DROP TABLE IF EXISTS user''')
cur.execute('''CREATE TABLE user
               (id integer primary key autoincrement, username text unique, password text, apikey text)''')

con.commit()
con.close()