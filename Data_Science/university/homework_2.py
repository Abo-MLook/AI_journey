from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# IoT sensor data
temperature = [25, 30, 35, 28, 32]
humidity = [60, 55, 70, 65, 50]

# Combine temperature and humidity into a 2D array
data = np.array(list(zip(temperature, humidity)))

# Apply K-Means Clustering (2 clusters)
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data)

# Get cluster labels for each data point
labels = kmeans.labels_
# Get cluster centers
centroids = kmeans.cluster_centers_

# Print results
print("Cluster Labels for each data point:")
print(labels)
print("\nCluster Centers (Temperature, Humidity):")
print(centroids)

# Plot the clustered data
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', label="Data Points")
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='x', s=200, label="Centroids")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("K-Means Clustering of IoT Data")
plt.legend()
plt.show()