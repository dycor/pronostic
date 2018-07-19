#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql7248339:XX1etS2T8C@sql7.freemysqlhosting.net:3306/sql7248339'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(255))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    password = db.Column(db.String(50))
    rank = db.Column(db.Integer)
    birthdate = db.Column(db.Date)
    admin = db.Column(db.Boolean)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date())
    time = db.Column(db.String(20))
    first_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    second_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    first_team_score = db.Column(db.Integer())
    second_team_score = db.Column(db.Integer())


class Pronostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_team_score = db.Column(db.Integer())
    second_team_score = db.Column(db.Integer())
    user_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    match_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    points = db.Column(db.Integer())
    second_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'))


@app.route('/')
def index():
    team = Team.query.all()
    # print('h')
    # pprint(team)
    return jsonify(team)

@app.route('/test')
def test():
    return "test"

if __name__ == '__main__':
    app.run(debug=True)