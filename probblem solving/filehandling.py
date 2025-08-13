from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
print(X)
y = np.array([1, 4, 5, 8])

model = LinearRegression()
model.fit(X, y)

print("Prediction for 5:", model.predict([[5]]))
