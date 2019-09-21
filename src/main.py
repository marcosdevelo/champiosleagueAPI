"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import db, User
from models import db, Player
from models import db, Teams
from flask_jwt_simple import (
    JWTManager, jwt_required, create_jwt, get_jwt_identity
)

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
# Setup the Flask-JWT-Simple extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


# Provide a method to create access tokens. The create_jwt()
# function is used to actually generate the token
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    params = request.get_json()
    screen_name = params.get('screen_name', None)
    password = params.get('password', None)

    if not screen_name:
        return jsonify({"msg": "Missing screen_name parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    # if username != 'test' or password != 'test':
    #     return jsonify({"msg": "Bad username or password"}), 401

    pupu=User.query.filter_by(screen_name=screen_name,password=password).first()
    if pupu == None:
        return jsonify({"msg": "Invalid credentials provided"}), 401



    # Identity can be any data that is json serializable
    ret = {'jwt': create_jwt(identity=screen_name)}
    return jsonify(ret), 200


# Protect a view with jwt_required, which requires a valid jwt
# to be present in the headers.
@app.route('/bubu', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    return jsonify({'hello_from': get_jwt_identity()}), 200

if __name__ == '__main__':
    app.run()
# Handle/serialize errors like a JSON object




@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_user():
    all_people = User.query.all()
    all_people_serialized = list(map(lambda x: x.serialize(), all_people))

    return jsonify(all_people_serialized), 200

@app.route('/teams', methods=['GET'])
def get_teams():
    all_people = Teams.query.all()
    all_people_serialized = list(map(lambda x: x.serialize(), all_people))


    return jsonify(all_people_serialized), 200

@app.route('/player', methods=['GET'])
def get_player():
    all_people = Player.query.all()
    all_people_serialized = list(map(lambda x: x.serialize(), all_people))


    return jsonify(all_people_serialized), 200



@app.route('/user', methods=['POST'])
def post_user():

    body = request.get_json()

    # if 'full_name' not in body:
    #     raise APIException('Hermamanazo te equivocaste en el full_name', status_code=400)

    # if body["email"].find('@') == -1:
    #     raise APIException('Mamita te falta un arroba en el email', status_code=400)

    user1 = User(full_name=body["full_name"], email=body["email"], screen_name=body["screen_name"], password=body["password"])
    db.session.add(user1)
    db.session.commit()

    return jsonify(user1.serialize()), 200

@app.route('/player', methods=['POST'])
def post_player():

    body = request.get_json()

    # if 'full_name' not in body:
    #     raise APIException('Hermamanazo te equivocaste en el full_name', status_code=400)

    # if body["email"].find('@') == -1:
    #     raise APIException('Mamita te falta un arroba en el email', status_code=400



    all_teams_with_id = list(Teams.query.filter_by(team_id=body["team_id"]))
    if(len(all_teams_with_id) > 0):
        user1 = Player(team_id=all_teams_with_id[0].id,name=body["name"],position=body["position"], image=body["image"], attack=body["attack"], defense=body["defense"], player_id=body["player_id"], season=body["season"], goals_total=body["goals_total"],goals_conceded=body["goals_conceded"], passes_total=body["passes_total"], tackles_total=body["tackles_total"], shots_total=body["shots_total"] )
        db.session.add(user1)
        db.session.commit()
        return jsonify(user1.serialize()), 200
    else:
        return jsonify({"message": "Team with id "+body["team_id"]+" not found"}), 400



@app.route('/teams', methods=['POST'])
def post_teams():

    body = request.get_json()




    team1 = Teams(team_id=body["team_id"],name=body["name"], teamLogo=body["teamLogo"], players=body["players"])

    #p = Player(teams=user1)
    #p2 = Player(teams=user1)

    db.session.add(team1)
    db.session.commit()

    return jsonify(team1.serialize()), 200

@app.route('/user/<int:id>', methods=['PUT'])
def put_persona(id):

    body = request.get_json()
    user1 = User.query.get(id)
    if user1 is None:
        raise APIException('User not found', status_code=404)

    if "full_name" in body:
        user1.full_name = body["full_name"]
    if "email" in body:
        user1.email = body["email"]
    if "phone" in body:
        user1.screen_name = body["screen_name"]
    if "password" in body:
        user1.password = body["password"]
    db.session.commit()

    return jsonify(user1.serialize()), 200

@app.route('/player/<int:id>', methods=['PUT'])
def put_player(id):

    body = request.get_json()
    user1 = Player.query.get(id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    if "team_id" in body:
        user1.team_id = body["team_id"]
    if "name" in body:
        user1.name = body["name"]
    if "position" in body:
        user1.position = body["position"]
    if "image" in body:
        user1.email = body["image"]
    if "attack" in body:
        user1.attack = body["attack"]
    if "defense" in body:
        user1.defense = body["defense"]
    if "player_id" in body:
        user1.player_id = body["player_id"]
    if "season" in body:
        user1.season = body["season"]
    if "goals_total" in body:
        user1.goals_total = body["goals_total"]
    if "goals_conceded" in body:
        user1.goals_conceded = body["goals_conceded"]
    if "passes_total" in body:
        user1.passes_total = body["passes_total"]
    if "tackles_total" in body:
        user1.tackles_total = body["tackles_total"]
    if "shots_total" in body:
        user1.shots_total = body["shots_total"]
    db.session.commit()

    return jsonify(user1.serialize()), 200

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_persona(id):

    user1 = User.query.get(id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user1)
    db.session.commit()

    return jsonify(user1.serialize()), 200

@app.route('/player/<int:id>', methods=['DELETE'])
def delete_player(id):

    user1 = Player.query.get(id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user1)
    db.session.commit()

    return jsonify(user1.serialize()), 200



# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
