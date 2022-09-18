import sqlite3
con = sqlite3.connect("custom_db.db")
print(con)
cur = con.cursor()
print(cur)
res = cur.execute('''CREATE TABLE IF NOT EXISTS user (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        email text NOT NULL,
                                        password text NOT NULL,
                                        firstname text NOT NULL,                                        
                                        lastname text NOT NULL)''')
print(res.fetchall())
res = cur.execute("SELECT * FROM user;")
print(res.fetchall())

