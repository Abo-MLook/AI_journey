
from sklearn.naive_bayes import GaussianNB

# Features: Temperature (°C), Humidity (%)
X_train = [
    [25, 60],  # Normal
    [40, 80],  # Faulty
    [30, 65],  # Normal
    [38, 75]   # Faulty
]

y_train = ["Normal", "Faulty", "Normal", "Faulty"]

iot_classifier = GaussianNB()
iot_classifier.fit(X_train, y_train)

new_device = [[35, 70]]  # Temperature = 35°C, Humidity = 70%
predicted = iot_classifier.predict(new_device)

print("=== IoT Device Status Prediction ===")
print(f"Input -> Temperature: 35°C, Humidity: 70%")
print(f"Predicted Device Status -> {predicted[0]}")
