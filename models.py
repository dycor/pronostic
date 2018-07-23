from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

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


class Pronostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_team_score = db.Column(db.Integer())
    second_team_score = db.Column(db.Integer())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    match_id = db.Column(db.Integer(), db.ForeignKey('match.id'))
    points = db.Column(db.Integer())
    first_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'))
    second_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'))