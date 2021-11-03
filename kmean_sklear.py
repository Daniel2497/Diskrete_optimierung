from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
X, y = make_blobs(n_samples=200, centers=4,
                   random_state=42)#, cluster.std=0.7)
print(X.shape)
plt.scatter(X[:,0],X[:,1])
#plt.show()


model=KMeans(4)
model.fit(X)
print(model.cluster_centers_)
centers = np.array(model.cluster_centers_)
plt.scatter(centers[:,0], centers[:,1], marker="x", color='r')
plt.show()