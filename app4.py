from flask import Flask, redirect, url_for, request
app = Flask(__name__)

import sqlalchemy as db

import sqlite3

from sqlite3 import Error

conn = sqlite3.connect('db22.sqlite')

@app.route('/')
def home():
   return "sveiki vartotojau"

@app.route('/maps/<mastelis>/<nomenklatura>')
def success(mastelis,nomenklatura):
   # irasyti i teksta faila
   irasas= open('atsakymas2.txt','a')
   irasas.write(mastelis)
   irasas.close()
   return 'welcome %s' % mastelis
   
   

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(port=5001,debug = True)