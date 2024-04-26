import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import model as orbit_predictor
from createData import time_steps, y_coords

import sys
sys.stdout.defaultencoding = 'utf-8'

orbit = pd.read_csv('./meteor_dataset.csv', index_col=0)
print(orbit)

if not (type(time_steps) == np.float32 and type(y_coords) == np.float32):
  print("Please convert the data to numpy float32 type .......!!!!")
  time_steps = np.asarray(time_steps, dtype=np.float32)
  y_coords = np.asarray(y_coords, dtype=np.float32)


orbit_predictor.fit(time_steps ,y_coords , epochs = 30)


# Evaluate your model 
print("Final loss value:",orbit_predictor.evaluate(time_steps, y_coords))
