# from ast import Return
from flask import Flask, redirect, url_for,render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html') 

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('success'))
   return render_template('login.html', error = error)

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
   app.run(debug = True)