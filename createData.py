import numpy as np
import pandas as pd

time_steps = np.arange(-10, +10, 0.01)

# create quadratic data
y_coords = np.square(time_steps)

dataframe= pd.DataFrame({"time_steps":time_steps, "Y coordinates":y_coords})
print(dataframe)
dataframe.to_csv('meteor_dataset.csv')