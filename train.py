import pandas as pd
import numpy as np
from model import model as orbit_predictor

orbit = pd.read_csv('./meteor_dataset.csv', index_col=0)
print(orbit)

# let's test againt last 1 minute of passing near earth

x_test = np.arange(-10, 11, 0.01)
