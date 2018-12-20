import sqlite3

from sqlite3 import Error

conn = sqlite3.connect('db1.sqlite')

c = conn.cursor()

c.execute('''

CREATE TABLE IF NOT EXISTS projects (
id integer PRIMARY KEY,
mastelis number NOT NULL,
nomenklatura text,
kiekis number);''')

data = c.fetchall()

print (data)