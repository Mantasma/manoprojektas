from flask import Flask, redirect, url_for, request
app = Flask(__name__)

import sqlite3

from sqlite3 import Error

conn = sqlite3.connect('db17.sqlite')

@app.route('/')
def home():
   return "sveiki vartotojau"

@app.route('/maps/<mastelis>/<nomenklatura>/<kiekis>/')
def success(mastelis,nomenklatura,kiekis):
   # irasyti i teksta faila
   irasas= open('atsakymas2.txt','a')
   irasas.write(mastelis)
   irasas.close()

   conn.execute("""INSERT INTO projects(mastelis, nomenklatura, kiekis) VALUES(?, ?, ?)""", (1,2,3))


   return 'welcome %s' % mastelis



if __name__ == '__main__':
   app.run(port=5001,debug = True)