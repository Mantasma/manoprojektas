from flask import Flask, redirect, url_for, request

import sqlite3

from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def home():
   return "sveiki vartotojau"

@app.route('/maps/<mastelis>/<nomenklatura>/<kiekis>/')
def success(mastelis,nomenklatura,kiekis):
   # parsisiunciamas irasas txt formatu
   irasas= open('atsakymas.txt','a')
   irasas.write(mastelis)
   irasas.close()
   
   conn = sqlite3.connect('db1.sqlite')

   conn = conn.cursor()

   conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (10000, "N-5", 5))
   conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (20000, "N-7", 20))
   conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (25000, "N-14", 3))
   conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (100000, "N-21", 1))
   conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (250000, "N-15", 7))

   conn.execute('''SELECT * FROM projects''')

   data = conn.fetchall()

   print (data)

   return 'welcome %s' % mastelis

if __name__ == '__main__':
   app.run(port=5001,debug = True)