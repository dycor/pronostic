#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import DateField, TimeField

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    firstname = StringField('Prénom', validators=[DataRequired()])
    lastname = StringField('Nom', validators=[DataRequired()])
    birthdate = StringField('Date de naissance', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirmation mot de passe')
    submit = SubmitField('Enregistrer')
    #
    # def validate_email(self, field):
    #     if Employee.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email is already in use.')
    #
    # def validate_username(self, field):
    #     if Employee.query.filter_by(username=field.data).first():
    #         raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Login')

class CreateMatchForm(FlaskForm):
    """
    Form for create a match
    """
    dateMatch = DateField('Start Date', format='%Y-%m-%d')
    # dateMatch = DateField('Date du match', format='%d-%m-%Y')
    timeMatch = TimeField('Heure du match')
    coteMatchDom = StringField('Cote match domicile', validators=[DataRequired()])
    coteMatchExt = StringField('Cote match extérieur', validators=[DataRequired()])
    submit = SubmitField('Valider')


