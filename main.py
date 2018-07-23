#! /usr/bin/python
# -*- coding:utf-8 -*-
# import settings
import flask

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from flask import Flask,render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_login import LoginManager
from flask_security import login_required,login_user,UserMixin,Security,SQLAlchemyUserDatastore
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask import Flask, session
from flask_session import Session
from sqlalchemy import update
from pprint import pprint

#Import models

from models import User
from models import Team
from models import Match
from models import Pronostic
from forms import LoginForm, RegistrationForm, CreateMatchForm
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'projetesgidufutur'

db = SQLAlchemy(app)
#
# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route('/match/<int:id>', methods=['GET', 'POST'])
def addPronostic(id):

    if request.method == 'POST':

        pronostic = Pronostic(first_team_score=request.form['first_team_score'],
                              second_team_score=request.form['second_team_score'],
                              user_id=session.get('id'),
                              match_id=id,
                              points=0,
                              first_team_id=request.form['first_team_id'],
                              second_team_id=request.form['second_team_id'])
        db.session.add(pronostic)
        db.session.commit()
        return redirect(url_for('index'))

    else :
        match = Match.query.filter_by(id=id).first()

        first_team = Team.query.filter_by(id = match.first_team_id).first()
        second_team = Team.query.filter_by(id = match.second_team_id).first()
        action = "/match/"+str(match.id)
        title = "Ajouter un pronostic"

    return render_template('pronostic/pronostic.html',match = match,first_team= first_team,second_team = second_team,action =action,title = title)

@app.route('/pronostic/<int:id>', methods=['GET', 'POST'])
def updatePronostic(id):

    if request.method == 'POST':
        pronostic = Pronostic.query.filter_by(id=id).first()
        pronostic.first_team_score = request.form['first_team_score']
        pronostic.second_team_score = request.form['second_team_score']

        db.session.commit()

        return redirect(url_for('index'))

    else :
        pronostic = Pronostic.query.filter_by(id=id).first()
        match = Match.query.filter_by(id=pronostic.match_id).first()
        first_team = Team.query.filter_by(id=match.first_team_id).first()
        second_team = Team.query.filter_by(id=match.second_team_id).first()
        action = "/pronostic/" + str(match.id)
        title = "Modifier un pronostic"



    return render_template('pronostic/pronostic.html',match = match,first_team= first_team,second_team = second_team,action =action,title = title,pronostic = pronostic)

@app.route('/mypronostics')
def mypronostics():
    pronostics = Pronostic.query.filter_by(user_id=session.get('id')).all()
    pronos = {}
    for pronostic in pronostics:
        team = Team.query.join(Match, Team.id == Match.first_team_id).first()
        team2 = Team.query.join(Match, Team.id == Match.second_team_id).first()
        pronostic.first_team_name = team.name
        pronostic.second_team_name = team2.name
        pronos[pronostic.id] = pronostic

    return render_template('pronostic/mypronostic.html',pronostics = pronostics)

@app.route('/')
def index():
    teams = Team.query.all()
    return render_template('teams.html', teams=teams)

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

@app.route('/createMatch', methods=["GET", "POST"])
def createMatch():
    form = CreateMatchForm()
    teams = Team.query.all()

    if request.method == 'POST':
        print('ok')
        match = Match(
            day = form.dateMatch.data,
            time = form.timeMatch.data,
            first_team_id = request.form.get('choiceTeamDom'),
            second_team_id = request.form.get('choiceTeamExt'),
            first_team_score = 0,
            second_team_score = 0,
            first_team_cote = form.coteMatchDom.data,
            second_team_cote = form.coteMatchExt.data
        )
        db.session.add(match)
        db.session.commit()

    return render_template('createMatch.html', form=form, teams=teams, title='Création d\'un match')


@app.route('/listMatch')
def listMatches():
    matchs = Match.query.all()
    matchDict = {}
    for match in matchs:
        team = Team.query.join(Match, Team.id == match.first_team_id).first()
        team2 = Team.query.join(Match, Team.id == match.second_team_id).first()
        match.first_team_name = team.name
        match.second_team_name = team2.name
        matchDict[match.id] = match

    return render_template('listMatch.html', matchs=matchs)

@app.route('/editMatch/<int:id>', methods=['GET', 'POST'])
def editMatches(id):
    matchs = Match.query.filter_by(id=id).first()
    form = CreateMatchForm()
    teams = Team.query.all()
    return render_template('editMatch.html', form=form, teams=teams, matchs=matchs)

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


if __name__ == '__main__':
    app.run(debug=True)

