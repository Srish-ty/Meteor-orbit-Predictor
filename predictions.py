import numpy as np
import matplotlib.pyplot as plt
from model import model as orbit_predictor

# let's test againt last 1 minute of passing near earth
x_test = np.arange(-10, 11, 0.01)

# function to plot predicted vs actual orbit
def plot_orbit(model_preds):
  axeslim = int(len(model_preds)/2)
  plt.plot(np.arange(-axeslim, axeslim + 1),np.arange(-axeslim, axeslim + 1)**2,color="mediumslateblue")
  plt.plot(np.arange(-axeslim, axeslim + 1),model_preds,color="orange")
  plt.axis([-40, 41, -5, 550])
  plt.legend(["Scientist's Orbit", 'Your orbit'],loc="lower left")
  plt.title("Predicted orbit vs Scientist's Orbit")
  plt.show()

# Predict the twenty minutes orbit
twenty_min_orbit = orbit_predictor.predict(np.arange(-10, 11))

# Plot the twenty minute orbit 
plot_orbit(twenty_min_orbit)