import sys
from urllib import request
from bs4 import BeautifulSoup
from flask import Flask, render_template
app = Flask(__name__)
 
#1
# @app.route('/')
# def hello_world():
#     return '<h1> Hello from Flask!! </h1>'
 
@app.route("/")
def home():
    return render_template('index.html', subject="안녕하세요. 반갑습니다. 조수현입니다.")
#1-1
@app.route('/<user>')
def hello(user):
    return '<h1> hello ' + user
 
#2
@app.route("/about")
def about():
    return render_template('busan1.html', image_file='img/2.jpg')
 
#3
@app.route("/show1")
def show1():
    return render_template('img_test1.html', image_file='img/1.jpg')   

@app.route("/show2")
def show2():
    return render_template('img_test2.html', image_file='img/3.jpg')   

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)