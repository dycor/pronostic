#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from forms import LoginForm, RegistrationForm, CreateMatchForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '2.7.0Kaaris'

db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(255))

    def __repr__(self):
        return '<Team %r>' % self.name

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
    first_team_cote = db.Column(db.Integer())
    second_team_cote = db.Column(db.Integer())


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
    teams = Team.query.all()
    return render_template('teams.html', teams=teams)

@app.route('/test')
def test():
    return "test"

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', form=form, title='Création d\'un compte')

@app.route('/createMatch', methods=["GET", "POST"])
def createMatch():
    form = CreateMatchForm()
    teams = Team.query.all()
    if form.validate_on_submit():
        match = Match(
            day = form.dateMatch.data,
            time = form.timeMatch.data,
            first_team_score = 0,
            second_team_score = 0,
            first_team_cote = form.coteMatchDom.data,
            second_team_cote = form.coteMatchExt.data
        )

        db.session.add(match)
        db.session.commit()
    return render_template('createMatch.html', form=form, teams=teams, title='Création d\'un match')

if __name__ == '__main__':
    app.run(debug=True)