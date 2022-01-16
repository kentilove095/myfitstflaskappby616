from flask import Flask, redirect, url_for,render_template,flash,url_for, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html') 

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['password'] != 'admin':
         error = 'Wrong SecretKey'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('success'))
   return render_template('login.html', error = error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
   app.run(debug = True)