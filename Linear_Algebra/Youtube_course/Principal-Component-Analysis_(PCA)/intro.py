import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets





iris = datasets.load_iris()
print(iris.data.shape)
print(iris.get("feature_names"))
print()
print(iris.data[0:6,:])


from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X = pca.fit_transform(iris.data)
print()
print(X.shape)
print()
print(X[0:6,:])

_ = plt.scatter(X[:, 0], X[:, 1])
plt.show()
#iris.target.shape
#iris.target[0:6]

unique_elements, counts_elements = np.unique(iris.target, return_counts=True)
np.asarray((unique_elements, counts_elements))
print()
print(list(iris.target_names))

_ = plt.scatter(X[:, 0], X[:, 1], c=iris.target)
plt.show()