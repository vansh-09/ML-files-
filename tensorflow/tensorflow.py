# === BASICS ===

# 1. Tensor creation and operations
import tensorflow as tf
import numpy as np

# Constants and Variables
t1 = tf.constant([[1, 2], [3, 4]])  # Constant tensor
t2 = tf.Variable([[5, 6], [7, 8]])  # Trainable variable

# Basic operations
add = tf.add(t1, t2)
mul = tf.multiply(t1, t2)
print("Addition Result:\n", add.numpy())
print("Multiplication Result:\n", mul.numpy())

# 2. Basic tensor info
print("Shape:", t1.shape)
print("Data type:", t1.dtype)

# 3. Converting numpy arrays to tensors
np_arr = np.array([[9, 10], [11, 12]])
tf_from_np = tf.convert_to_tensor(np_arr)


# === DATA PIPELINE ===

# 4. tf.data for loading and batching
data = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5, 6])
data = data.map(lambda x: x * 2).batch(2)
for batch in data:
    print("Batch:", batch.numpy())


# === MODELING ===

# 5. Sequential model (basic)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),
    Dense(8, activation='relu'),
    Dense(1)
])

model.summary()


# 6. Functional API (advanced structure)
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Concatenate

input1 = Input(shape=(4,))
x = Dense(16, activation='relu')(input1)
x = Dense(8, activation='relu')(x)
out = Dense(1)(x)
model_func = Model(inputs=input1, outputs=out)
model_func.summary()


# === TRAINING ===

# 7. Compile, fit, evaluate
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Dummy training data
X_train = np.random.rand(100, 4)
y_train = np.random.rand(100, 1)

# Fit model
model.fit(X_train, y_train, epochs=5, batch_size=8)

# Evaluate model
loss, mae = model.evaluate(X_train, y_train)
print("Loss:", loss, "MAE:", mae)


# === CALLBACKS ===

# 8. Callbacks (EarlyStopping + TensorBoard)
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard

callbacks = [
    EarlyStopping(monitor='loss', patience=3),
    TensorBoard(log_dir='./logs')
]

model.fit(X_train, y_train, epochs=10, batch_size=8, callbacks=callbacks)


# === SAVING AND LOADING ===

# 9. Saving and loading model
model.save('my_model.keras')  # Save in Keras format

loaded_model = tf.keras.models.load_model('my_model.keras')
pred = loaded_model.predict(X_train[:5])
print("Predictions from loaded model:\n", pred)


# === TENSORBOARD (Visualization) ===

# Launch tensorboard in terminal:
# !tensorboard --logdir=./logs

# Visit http://localhost:6006 to see training curves, model graphs etc.


# === NOTES ===
# - All examples here use random or dummy data.
# - Replace these with real datasets (like from sklearn or Kaggle) for projects.
# - This file is meant to be your foundation to explore TensorFlow confidently.
# - Every section can be turned into its own notebook/module in the repo.
