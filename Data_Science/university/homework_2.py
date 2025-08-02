from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Data for clustering
temperature = [25, 30, 35, 28, 32]
humidity = [60, 55, 70, 65, 50]

# Combine data into a 2D array
data = np.array(list(zip(temperature, humidity)))

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data)

# Get and print results
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("Cluster Labels for each data point:")
print(labels)

print("\nCluster Centers (Temperature, Humidity):")
print(centroids)

# Plot the clusters and centroids
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', label="Data Points")
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='x', s=200, label="Centroids")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("K-Means Clustering of IoT Data")
plt.legend()
plt.show()
