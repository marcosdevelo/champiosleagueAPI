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
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

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

@app.route('/player', methods=['GET'])
def get_player():
    all_people = Player.query.all()
    all_people_serialized = list(map(lambda x: x.serialize(), all_people))


    return jsonify(all_people_serialized), 200

@app.route('/teams', methods=['GET'])
def get_team():
    all_people = Teams.query.all()
    all_people_serialized = list(map(lambda x: x.serialize(), all_people))


    return jsonify(all_people_serialized), 200

@app.route('/user', methods=['POST'])
def post_persona():

    body = request.get_json()

    # if 'full_name' not in body:
    #     raise APIException('Hermamanazo te equivocaste en el full_name', status_code=400)

    # if body["email"].find('@') == -1:
    #     raise APIException('Mamita te falta un arroba en el email', status_code=400)

    user1 = User(full_name=body["full_name"], email=body["email"], screen_name=body["screen_name"], password=body["password"])
    db.session.add(user1)
    db.session.commit()

    return jsonify(user1.serialize()), 200

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

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_persona(id):

    user1 = User.query.get(id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user1)
    db.session.commit()

    return jsonify(user1.serialize()), 200



# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
