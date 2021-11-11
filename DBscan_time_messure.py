from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
import time
time_values=[]
#Für mehr als 10^5 Punkte eleminiert sich das Programm immer selbst
#Interpolation mit Punkten bis 10^5
#100,200,400,800,1600,3200,6400,128000,256000,512000(10 Punkte, 2x)
for i in range(10):#10
    X, y = make_blobs(n_samples=100*(2**(i)), centers=4,
                   random_state=42)#, cluster.std=0.7)



    #print(X.shape)
    start = time.time()
    #plt.show()
    clustering = DBSCAN(eps=3, min_samples=2).fit(X)
    #print(clustering.labels_)
    end = time.time()
    elapsed=end-start
    time_values.append(elapsed)
time_values_normalised=[]
problemsize=[]
for i in range(10):#10
    time_values_normalised.append(time_values[i]/time_values[0])
    problemsize.append(100*(2**i))
    #plt.scatter(centers[:,0], centers[:,1], marker="x", color='r')
    #xsquar.append(2**(2*i))
print("Problemgröße:")
print(problemsize)
print("Berechnungszeiten")
print(time_values)
print("Berechnungszeiten normalisiert auf kleinste Problemgröße")
print(time_values_normalised)
#print(xsquar)

log_time_values_normalised=[]
#for i in range(10):
log_time_values_normalised=np.log2(time_values_normalised)
    #plt.show()
print("Log2 auf normalisierte Berechnungzeiten")
print(log_time_values_normalised)

#Plot Results
#plt.plot(log_time_values_normalised)
#plt.plot(range(8))#10
#zz=range(10)*2
#plt.plot(range(0,16,2))#0,20,2
#plt.plot(range(10))
#plt.show()
