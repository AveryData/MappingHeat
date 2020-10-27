import pandas as pd
import json

from flask import (
    Blueprint, request
)
from .db import get_db

bp = Blueprint('stats', __name__, url_prefix='/stats')

pitching_data = pd.DataFrame()

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