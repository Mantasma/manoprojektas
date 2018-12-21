from flask import Flask, redirect, url_for, request

import sqlite3

from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def home():
   return "sveiki vartotojau"

@app.route('/maps/<mastelis>/<nomenklatura>/<kiekis>/')
def success(mastelis,nomenklatura,kiekis):
   conn = sqlite3.connect('db1.sqlite')
   conn = conn.cursor()
   conn.execute('''INSERT INTO projects(mastelis, nomenklatura,kiekis) VALUES(?, ?, ?)''', (mastelis, nomenklatura, kiekis))

   conn.close()

   return 'sekmingai isirase'

if __name__ == '__main__':
   app.run(port=5001,debug = True)