import pandas as pd
from sklearn.linear_model import LogisticRegression

from .db import get_db

cache = {}

def init_model():
  df = pd.read_sql("SELECT player_name, pitch_type, CAST(release_speed AS float) as release_speed, zone, description FROM pitching_data WHERE zone IS NOT NULL", get_db())
  features = ['player_name', 'pitch_type', 'release_speed', 'zone']

  x_norm = df[features]
  x = pd.get_dummies(x_norm)
  y = df['description'].apply(lambda d: hot_encode_des(d))

  model = LogisticRegression(max_iter=500)
  model.fit(x, y)

  cache['model'] = model
  cache['x_cols'] = x.columns

def get_model():
  if 'model' not in cache:
    init_model()
  return cache['model']

def get_xcols():
  if 'x_cols' not in cache:
    init_model()
  return cache['x_cols']

def predict(params):
  features_df = pd.get_dummies(pd.DataFrame(params))
  features_df = features_df.reindex(columns=get_xcols(), fill_value=0)
  model = get_model()
  return model.predict(features_df)

def hot_encode_des(x):
  if x == 'hit_into_play_no_out' or x == 'hit_into_play_score':
    return 1
  return 0