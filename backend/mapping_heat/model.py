import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from flask import g
import pickle

from .db import get_db

cache = {}

def init_model():
  filename = '../model/pitch_prob.sav'
  loaded_model = pickle.load(open(filename, 'rb'))
  x = pd.read_csv('../model/df_shell.csv')

  cache['model'] = loaded_model
  cache['x_cols'] = x.columns

def get_model():
  if 'model' not in cache:
    init_model()
  return cache['model']

def get_xcols():
  if 'x_cols' not in cache:
    init_model()
  return cache['x_cols']
#
def predict(params):
  features_df = pd.get_dummies(pd.DataFrame(params))
  features_df = features_df.reindex(columns=get_xcols(), fill_value=0)
  model = get_model()
  return model.predict_proba(features_df)

def hot_encode_des(x):
  if x == 'hit_into_play_no_out' or x == 'hit_into_play_score':
    return 1
  return 0