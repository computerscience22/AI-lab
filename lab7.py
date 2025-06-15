# Linear

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Example data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# Create linear regression object
model = linear_model.LinearRegression()

# Train the model
model.fit(x, y)

# Make predictions
y_pred = model.predict(x)

# Print coefficients
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Plottingpi
plt.scatter(x, y, color="black")
plt.plot(x, y_pred, color="blue", linewidth=3)
plt.show()


# Logistic
import numpy as np
from sklearn.linear_model import LogisticRegression

# Example data
# X: Feature (e.g., tumor size in cm)
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
# y: Target (0 = not cancerous, 1 = cancerous)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Create and train the logistic regression model
logr = LogisticRegression()
logr.fit(X, y)

# Predict for a new sample (e.g., tumor size 3.46 cm)
predicted = logr.predict(np.array([3.46]).reshape(-1, 1))
print("Prediction (0=No, 1=Yes):", predicted[0])
