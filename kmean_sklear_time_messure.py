from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import time
time_values=[]
for i in range(6):
    X, y = make_blobs(n_samples=10**(i+2), centers=4,
                   random_state=42)#, cluster.std=0.7)
    start = time.time()
    model=KMeans(4)
    model.fit(X)
    centers = np.array(model.cluster_centers_)
    end = time.time()
    elapsed=end-start
    time_values.append(elapsed)

time_values_normalised=[]

for i in range(6):
    time_values_normalised.append(time_values[i]/time_values[0])
print(time_values)
print(time_values_normalised)