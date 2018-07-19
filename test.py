#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import migrations.Team
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'


@app.route('/')
def index():
    return "Hello !"

def test():
    return "test"

if __name__ == '__main__':
    app.run(debug=True)