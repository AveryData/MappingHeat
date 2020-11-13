import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from flask import g

from .db import get_db

def init_model():
  df = pd.read_sql("SELECT * FROM pitching_data LIMIT 1000", get_db())
  features = ['player_name', 'pitch_type', 'release_speed', 'zone']

  df_sanitized = df[~df.zone.isnull()]

  x_norm = df_sanitized[features]
  x = pd.get_dummies(x_norm)
  y = df_sanitized['description'].apply(lambda d: hot_encode_des(d))

  model = LogisticRegression(max_iter=500)
  model.fit(x, y)

  g.model = model
  g.x_cols = x.columns

  return model, x.columns

def get_model():
  if 'model' not in g:
    init_model()
  return g.model

def get_xcols():
  if 'x_cols' not in g:
    init_model()
  return g.x_cols

def predict(params):
  features_df = pd.get_dummies(pd.DataFrame(params))
  features_df = features_df.reindex(columns=get_xcols(), fill_value=0)
  model = get_model()
  return model.predict(features_df)

def hot_encode_des(x):
  if x == 'hit_into_play_no_out' or x == 'hit_into_play_score':
    return 1
  return 0