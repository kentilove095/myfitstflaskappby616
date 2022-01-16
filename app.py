from ast import Return
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello My First Application"
@app.route('/hello')
def hello_world():
       return 'hello world'
app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)