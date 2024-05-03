from keras.models import Sequential
from keras.layers import Dense

model = Sequential([
    Dense(10, input_shape=(1,), activation='relu'),
    Dense(5, activation='relu'),
    Dense(1)
])

#  input layer and a hidden layer with 10 neurons
#model.add(Dense(10, input_shape=(1,), activation="relu"))
#model.add(Dense(5, activation="relu"))

#  1-neuron output layer
#model.add(Dense(1))


# Compile your model
model.compile(optimizer = 'adam', loss = 'mse')

# Summarising
model.summary()