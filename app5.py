from flask import Flask, redirect, url_for, request
app = Flask(__name__)

import sqlite3

from sqlite3 import Error


@app.route('/')
def home():
   return "sveiki vartotojau"

@app.route('/maps/<mastelis>/<nomenklatura>/<kiekis>/')
def success(mastelis,nomenklatura,kiekis):
   # irasyti i teksta faila
   irasas= open('atsakymas2.txt','a')
   irasas.write(mastelis)
   irasas.close()

   
   conn = sqlite3.connect('db21.sqlite')

   conn.execute('''

CREATE TABLE IF NOT EXISTS projects (
id integer PRIMARY KEY,
mastelis number NOT NULL,
nomenklatura text,
kiekis number);''')

   return 'welcome %s' % mastelis

if __name__ == '__main__':
   app.run(port=5001,debug = True)