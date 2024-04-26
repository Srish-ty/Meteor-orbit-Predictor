import pandas as pd
from model import model as orbit_predictor

orbit = pd.read_csv('./dataset/orbit.csv')
orbit.head()