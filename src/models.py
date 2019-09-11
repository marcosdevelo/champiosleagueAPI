from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    screen_name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Person %r>' % self.email

    def serialize(self):
        return {
            "id":self.id,
            "full_name": self.full_name,
            "email": self.email,
            "screen_name": self.screen_name,
            "password": self.password,
            }

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), unique=True, nullable=False)
    team_id = db.Column(db.String(120), unique=True, nullable=False)
    computer_team_id = db.Column(db.String(100), unique=True, nullable=False)



    def __repr__(self):
        return '<Person %r>' % self.computer_team_id

    def serialize(self):
        return {
            "id":self.id,
            "user_id": self.full_name,
            "email": self.email,
            "team_id": self.screen_name,
            "computer_team_id": self.password,
            }

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    game_id = db.Column(db.String(120), unique=True, nullable=False)



    def __repr__(self):
        return '<Person %r>' % self.slug

    def serialize(self):
        return {
            "id":self.id,
            "slug": self.slug,
            "game_id": self.game_id,
            }

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    team_id = db.Column(db.String(120), unique=True, nullable=False)
    fixture_id = db.Column(db.String(120), unique=True, nullable=False)
    activity_id = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Person %r>' % self.team_id

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "team_id": self.team_id,
            "fixture_id": self.fixture_id,
            "activity_id": self.activity_id,
            }

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.String(80), unique=True, nullable=False)
    attack = db.Column(db.String(80), unique=True, nullable=False)
    defense = db.Column(db.String(80), unique=True, nullable=False)
    player_id = db.Column(db.String(120), unique=True, nullable=False)
    team_goals = db.Column(db.String(100), unique=True, nullable=False)
    team_passes = db.Column(db.String(120), unique=True, nullable=False)
    team_fouls = db.Column(db.String(120), unique=True, nullable=False)
    team_blocked_shots = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Person %r>' % self.attack

    def serialize(self):
        return {
            "id":self.id,
            "team_id":self.team_id,
            "attack":self.attack,
            "defense": self.defense,
            "player_id": self.player_id,
            "team_goals": self.team_goals,
            "team_passes": self.team_passes,
            "team_fouls": self.team_fouls,
            "team_blocked_shots": self.team_blocked_shots,
            }