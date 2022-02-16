from app import app
from flask import render_template
from flask import Blueprint
site = Blueprint('site, __name__')
@site.route('/')
def index():
    return "homepage"

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/')
def page_2():
    return "This is page 2"


@app.route('/')
def page_3():
    return "This is page "
