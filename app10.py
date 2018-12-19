import sqlite3

from sqlite3 import Error

conn = sqlite3.connect('n4.sqlite')

c = conn.cursor()

c.execute('''

CREATE TABLE IF NOT EXISTS projects (
id integer PRIMARY KEY,
mastelis number NOT NULL,
nomenklatura text,
kiekis number);''')

c.execute("""INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)""", (1,2,3))

c.execute('''SELECT * FROM projects''')

data = c.fetchall()

print (data)