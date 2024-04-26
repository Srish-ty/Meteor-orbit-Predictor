import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import model as orbit_predictor
from createData import time_steps, y_coords

import sys
sys.stdout.defaultencoding = 'utf-8'

orbit = pd.read_csv('./meteor_dataset.csv', index_col=0)
print(orbit)


orbit_predictor.fit(time_steps ,y_coords , epochs = 30)


# Evaluate your model 
print("Final loss value:",orbit_predictor.evaluate(time_steps, y_coords))
