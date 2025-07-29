import random
import matplotlib.pyplot as plt

# Generate hourly readings (12 hours)
time_labels = [f"{h}:00" for h in range(1, 13)]
sensor_temp = [round(random.uniform(20.0, 30.0), 2) for _ in time_labels]

# Display data in table format
print("Time\tTemperature (°C)")
for t, temp in zip(time_labels, sensor_temp):
    print(f"{t}\t{temp}")

# Plot
plt.figure(figsize=(8, 4))
plt.plot(time_labels, sensor_temp, linestyle='--', marker='s', color='green')
plt.title("12-Hour IoT Sensor Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
