#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/login/<name>')
def login(name):
    return f"Welcome {name}, you are logged in."

if __name__ == '__main__':
             app.run()