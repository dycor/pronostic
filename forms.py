from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError,DateField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    firstname = StringField('Prénom', validators=[DataRequired()])
    lastname = StringField('Nom', validators=[DataRequired()])
    birthdate = DateField('Date de naissance', format='%d-%m-%Y',validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirmation mot de passe')
    submit = SubmitField('Enregistrer')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Login')