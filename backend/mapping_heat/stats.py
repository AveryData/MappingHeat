import pandas as pd
import json

from flask import (
    Blueprint, request
)
from .db import get_db
from .model import predict

bp = Blueprint('stats', __name__, url_prefix='/stats')

pitching_data = pd.DataFrame()

@bp.route('/pitchers/names', methods=['GET'])
def pitcher_names():
    name_query = "SELECT DISTINCT player_name FROM pitching_data ORDER BY player_name ASC"
    names = [row[0] for row in get_db().execute(name_query).fetchall()]

    return json.dumps(names)

@bp.route('/pitcher', methods=['GET'])
def pitcher():
    name = request.args.get('name')
    pitch_query = "SELECT * FROM pitching_data WHERE player_name = '{}'".format(name)
    pitcher_data = [dict(row) for row in get_db().execute(pitch_query).fetchall()]

    return json.dumps(pitcher_data)

@bp.route('/pitcher/pitch', methods=['GET'])
def pitch_type():
    name = request.args.get('name')
    pitch = request.args.get('pitch')
    #TODO check if above params exists since we are explicitly assinging
    pitch_query = "SELECT * FROM pitching_data WHERE player_name = '{}' and pitch_type = '{}'".format(name, pitch)
    pitch_data = [dict(row) for row in get_db().execute(pitch_query).fetchall()]

    return json.dumps(pitch_data)

@bp.route('/pitcher/feature', methods=['GET'])
def pitch_feature():
    name = request.args.get('name')
    feature = request.args.get('feature')
    feature_value = request.args.get('value')
    feature_query = "SELECT * FROM pitching_data WHERE player_name = {} and {} = {}".format(name, feature, feature_value)
    print(feature_query)
    pitch_data = [dict(row) for row in get_db().execute(feature_query).fetchall()]

    return json.dumps(pitch_data)

@bp.route('/predict', methods=['GET'])
def predict_zones():
    name = [request.args.get('name')]
    pitch = [request.args.get('pitch')]
    speed = [request.args.get('speed', type=float)]

    results = {}
    for i in range(1, 15):
        if i != 10:
            zone = str(float(i))
            prediction = predict({'player_name': name, 'pitch_type': pitch, 'release_speed': speed, 'norm_zone': zone})
            results[i] = prediction.item(1)

    return json.dumps(results)