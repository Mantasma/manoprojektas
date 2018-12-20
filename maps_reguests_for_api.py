from flask import Flask, redirect, url_for, request

import sqlite3

from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def home():
   return "sveiki vartotojau"

@app.route('/maps/<mastelis>/<nomenklatura>/<kiekis>/')
def success(mastelis,nomenklatura,kiekis):
   # irasyti i teksta faila
   irasas= open('atsakymas2.txt','a')
   irasas.write(mastelis)
   irasas.close()
   
   conn = sqlite3.connect('db23.sqlite')

   conn = conn.cursor()

   conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (1000, "N-5", 5))
   conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (1000, "N-7", 5))

   conn.execute('''SELECT * FROM projects''')

   data = conn.fetchall()

   print (data)

   return 'welcome %s' % mastelis

if __name__ == '__main__':
   app.run(port=5001,debug = True)