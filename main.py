#! /usr/bin/python
# -*- coding:utf-8 -*-
# import settings
import flask

from flask import Flask,render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from forms import LoginForm, RegistrationForm
from flask_login import LoginManager
from flask_security import login_required,login_user,UserMixin,Security,SQLAlchemyUserDatastore
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask import Flask, session
from flask_session import Session


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '2.7.0Kaaris'

db = SQLAlchemy(app)
#
# login_manager = LoginManager()
# login_manager.init_app(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(255))

    def __init__(self, id, name,image):
        self.id = id
        self.name = name
        self.image = image


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    password = db.Column(db.String(50))
    rank = db.Column(db.Integer)
    birthdate = db.Column(db.Date)
    admin = db.Column(db.Boolean)

    def verify_password(self, pwd):
        return self.password == pwd

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
    id = session.get('id')
    # print(user)
    return str(id)
    teams = Team.query.all()
    return render_template('teams.html', teams=teams)

@app.route('/test')
def test():
    return bcrypt.generate_password_hash('test',31)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()


    if form.validate_on_submit():
        user = User(email=form.email.data,
                    firstname=form.firstname.data,
                    lastname=form.firstname.data,
                    birthdate=form.birthdate.data,
                    password= form.password.data,
                    admin= 0)


        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('auth/register.html', form=form, title='Création d\'un compte')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            session['id'] = user.id
            session['email'] = user.email
            session['firstname'] = user.firstname
            session['lastname'] = user.lastname
            session['rank'] = user.rank
            session['birthdate'] = user.birthdate
            session['admin'] = user.admin

            return redirect(url_for('index'))


    return render_template('auth/login.html', form=form, title='Log in')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
