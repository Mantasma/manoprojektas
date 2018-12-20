import sqlite3

from sqlite3 import Error

conn = sqlite3.connect('db23.sqlite')

conn = conn.cursor()

conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (1000, "N-5", 5))
conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (1000, "N-6", 5))

conn.execute('''SELECT * FROM projects''')

data = conn.fetchall()

print (data)
