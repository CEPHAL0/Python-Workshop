import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 6, 9, 12, 15])

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Trained and Saved")