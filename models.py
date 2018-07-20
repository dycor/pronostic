# from main import app
# from app import db
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
        """
        Check if hashed password matches actual password
        """
        return self.password == pwd

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

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