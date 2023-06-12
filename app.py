from flask import Flask

app = Flask(__name__)

@app.route('/app/')
def first():
    return '<h1>Hello, first page</h1>'

@app.route('/app/home')
def home():
    return '<h1>Hello, Homepage !!! content for the homepage</h1>'

@app.route('/app/aboutus')
def about():
    return '<h1>about us page of the company!!!</h1>'

@app.route('/app/contactus')
def contact():
    return '<h1>contact us for more services</h1>'

@app.route('/app/login/')
def login():
    return '<h1>login page </h1>'

@app.route('/app/login/user')
def login_user():
    return '<h1>Hello, Amn... this is for testing purpose</h1>'


