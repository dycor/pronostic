#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import migrations.Team
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello !"

if __name__ == '__main__':
    app.run(debug=True)