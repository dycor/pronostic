#! /usr/bin/python
# -*- coding:utf-8 -*-
# import settings
import flask

<<<<<<< HEAD
from flask import Flask,render_template, request, redirect,url_for
=======
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask,render_template
>>>>>>> 3c6495851d02c1a07097b36656f6346bdd559a08
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

#Import models
from models.User import User
from models.Team import Team
from models.Match import Match
from models.Pronostic import Pronostic


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'projetesgidufutur'

db = SQLAlchemy(app)
#
# login_manager = LoginManager()
# login_manager.init_app(app)


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

if __name__ == '__main__':
    app.run(debug=True)
