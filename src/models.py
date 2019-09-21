from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    screen_name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)


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
            "user_id": self.user_id,
            "team_id": self.team_id,
            "computer_team_id": self.computer_team_id,
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
    teamLogo= db.Column(db.String(300), unique=True, nullable=False)
    players = db.relationship('Player',backref='teams', lazy=True)

    def __repr__(self):
        return '<Person %r>' % self.teamLogo

    def serialize(self):
        return {
            "id":self.id,
            "name": self.name,
            "team_id": self.team_id,
            "teamLogo": self.teamLogo,
            "players": list(map(lambda x: x.serialize(), self.players))
            }

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id= db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    name= db.Column(db.String(80), unique=False, nullable=False)
    position= db.Column(db.String(80), unique=False, nullable=False)
    image= db.Column(db.String(200), unique=False, nullable=False)
    attack = db.Column(db.String(80), unique=False, nullable=False)
    defense = db.Column(db.String(80), unique=False, nullable=False)
    player_id = db.Column(db.String(120), unique=False, nullable=False)
    season = db.Column(db.String(80), unique=False, nullable=False)
    goals_total = db.Column(db.String(100), unique=False, nullable=False)
    goals_conceded = db.Column(db.String(100), unique=False, nullable=False)
    passes_total = db.Column(db.String(120), unique=False, nullable=False)
    tackles_total = db.Column(db.String(120), unique=False, nullable=False)
    shots_total = db.Column(db.String(120), unique=False, nullable=False)


    def __repr__(self):
        return '<Person %r>' % self.attack

    def serialize(self):
        return {
            "id":self.id,
            "team_id":self.team_id,
            "name":self.name,
            "position":self.position,
            "image":self.image,
            "attack":self.attack,
            "defense": self.defense,
            "player_id": self.player_id,
            "season": self.season,
            "goals_total": self.goals_total,
            "goals_conceded": self.goals_conceded,
            "passes_total": self.passes_total,
            "tackles_total": self.tackles_total,
            "shots_total": self.shots_total,
            }