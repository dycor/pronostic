#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '2.7.0Kaaris'

db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(255))

    # def __repr__(self):
    #     return '<Team %r>' % self.name
    def __init__(self, id, name,image):
        self.id = id
        self.name = name
        self.image = image


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    password = db.Column(db.String(50))
    rank = db.Column(db.Integer)
    birthdate = db.Column(db.Date)
    admin = db.Column(db.Boolean)

    def __init__(self, id, email,firstname,lastname,password,rank,birthdate,admin):
        self.id = id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.rank = rank
        self.birthdate = birthdate
        self.admin = admin


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date())
    time = db.Column(db.String(20))
    first_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    second_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    first_team_score = db.Column(db.Integer())
    second_team_score = db.Column(db.Integer())

    def __init__(self, id, day, time, first_team_id, second_team_id, first_team_score, second_team_score):
        self.id = id
        self.day = day
        self.time = time
        self.first_team_id = first_team_id
        self.second_team_id = second_team_id
        self.first_team_score = first_team_score
        self.second_team_score = second_team_score

class Pronostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_team_score = db.Column(db.Integer())
    second_team_score = db.Column(db.Integer())
    user_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    match_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    points = db.Column(db.Integer())
    second_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'))


    def __init__(self, first_team_score, second_team_score, user_id, match_id, points, second_team_id):
        self.first_team_score = first_team_score
        self.second_team_score = second_team_score
        self.user_id = user_id
        self.match_id = match_id
        self.points = points
        self.second_team_id = second_team_id

@app.route('/')
def index():
    teams = Team.query.all()
    return render_template('teams.html', teams=teams)

@app.route('/test')
def test():
    return "test"

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', form=form, title='Création d\'un compte')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form, title='Log in')

if __name__ == '__main__':
    app.run(debug=True)