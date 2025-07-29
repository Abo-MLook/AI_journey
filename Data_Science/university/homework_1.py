import random
import time
from tabulate import tabulate

data = []
for i in range(5):
    sensor_id = f"S{random.randint(100,999)}" # id for sensor
    temperature = round(random.uniform(15.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 90.0), 2)
    status = "High" if temperature > 30 else "Normal"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    data.append([sensor_id, temperature, humidity, status, timestamp])

# table for displaying
headers = ["Sensor ID", "Temperature (°C)", "Humidity (%)", "Status", "Timestamp"]
print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
