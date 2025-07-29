from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Data
temperature = np.array([22, 25, 28, 30]).reshape(-1, 1)
humidity = np.array([45, 50, 55, 60])

# Train the Linear Regression model
model = LinearRegression()
model.fit(temperature, humidity)

# Predict humidity
predicted_humidity = model.predict(temperature)
print("Predicted Humidity:", predicted_humidity)

# Plot the results
plt.scatter(temperature, humidity, color='blue', label='Data Points')
plt.plot(temperature, predicted_humidity, color='red', label='Regression Line')
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Linear Regression for IoT Data")
plt.legend()
plt.show()
