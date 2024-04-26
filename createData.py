import numpy as np
import pandas as pd

time_steps = np.arange(-100, +101, 0.01)

# create quadratic data
y_coords = np.square(time_steps)

# our dataframe
dataframe = pd.DataFrame({"time_steps":time_steps, "Y coordinates":y_coords})
print(dataframe)

# create csv file using the dataset
dataframe.to_csv('meteor_dataset.csv')