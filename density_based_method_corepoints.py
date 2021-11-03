from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.cluster import KMeans

#Task to do: 
#Es kann passieren, dass sich zwei Gruppen von Corepoints bilden, welche
#eigentlich zusammengehören
#Bsp. Corepoint x1=(1,0), x3=(1.5,0), x2=(2,0), epsilon=0.6
#wird erst x1 der einen gruppe, x2 der anderen Gruppe zugeordnet
#erst durch die spätere Entdeckung von x3 wird klar, dass x1 und x2 
#zusammen gehören.
#Lösungvorschlag, x3 zu mehren Gruppen zuweisen und am Ende die Gruppe
#miteinander vergleichen

N=250
X, y = make_blobs(n_samples=N, centers=4,
                   random_state=42)#, cluster.std=0.7)
print(X.shape)
plt.scatter(X[:,0],X[:,1])
#plt.show()
epsilon=0.5
#print(y)
corepoints=[]
isolatedpoints=[]
isolatedpoints_scnd_order=[] #Andere Punkte, aber keine Corepoints in der Umgebung
neighbor_and_corepoints=[]

#Erstellung der Isolatedpoints
for i in range(N):
    isolated=True
    for j in range(0,i):
        if ((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)<epsilon:
            isolated=False
    for j in range(i+1,N):
        if ((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)<epsilon:
            isolated=False
    if isolated:
        isolatedpoints.append(i)

#Corepoints and Neigbors
for i in range(N):
    counter=0
    neighbors=[]
    for j in range(0,i):
        if ((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)<epsilon:
            counter+=1
            neighbors.append(j)
    for j in range(i+1,N):
        if ((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)<epsilon:
            counter+=1
            neighbors.append(j)
    notinList=True
    continue_search=True
    for a in corepoints:
        for s in a:
            for neighbor in neighbors:
                if s==neighbor and counter>3 and continue_search:
                    a.append(i)
                    notinList=False
                    continue_search=False #Ausklammerung macht das Programm sehr langsam
    if notinList:
        if counter>3:
            a=[i]
            corepoints.append(a)
    #Falls i kein Corepoint ist, finde seinen nächsten Nachbar Corepoint oder ordne es isolated scnd Order zu
    if counter <=3 and counter > 0:
        closest_distance=100000
        closest_couple=[]
        for s in neighbors: #finde den Corpoint in neighbors
            counter=0
            #Überprüfe ob s corepoint ist
            for j in range(0,s):
                if ((X[s,0]-X[j,0])**2+(X[s,1]-X[j,1])**2)<epsilon:
                    counter+=1
            for j in range(s+1,N):
                if ((X[s,0]-X[j,0])**2+(X[s,1]-X[j,1])**2)<epsilon:
                    counter+=1
            if counter >3:
                if ((X[i,0]-X[s,0])**2-(X[i,1]-X[s,1])**2)<closest_distance:
                    closest_couple=[i,s]
                    closest_distance=((X[i,0]-X[s,0])**2-(X[i,1]-X[s,1])**2)
        if closest_couple ==[]:
            isolatedpoints_scnd_order.append(i)
        else:
            neighbor_and_corepoints.append(closest_couple)



print(neighbor_and_corepoints)                    
#print(corepoints)
colarr=["aliceblue","azure","black","white","blueviolet","brown","gray","yellow","gold","green"]
collcounter=0
#Markiere Corepoints
for a in corepoints:
    random.seed(collcounter)
    col= ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]#Farben zufällig wählen
    for s in a:        
        #plt.scatter(X[s,0],X[s,1],marker="P",color=colarr[collcounter%10])
        plt.scatter(X[s,0],X[s,1],marker="P",color=col)
        #Markiere Nachbar von Corepoint, welche kein Corepoint ist
        for couple in neighbor_and_corepoints:
            if couple[1]==s:
                #plt.scatter(X[couple[0],0],X[couple[0],1],marker="x",color=colarr[collcounter%10])
                plt.scatter(X[couple[0],0],X[couple[0],1],marker="x",color=col)
    collcounter=collcounter+1
#Markieren Isolatedpoints
for s in isolatedpoints:
    plt.scatter(X[s,0],X[s,1],marker="x",color="red")
#Markiere Isolatedpoints scnd order
for s in isolatedpoints_scnd_order:
    plt.scatter(X[s,0],X[s,1],marker="P",color="red")
#print(X[i,1],X[i,0])
print("Die Anzahl der verschiedenen Gruppen von Corepoints beträgt: ",len(corepoints))
corenumber=0
for a in corepoints:
    corenumber+=len(a)
print(corenumber)
#model=KMeans(4)
#model.fit(X)
#print(model.cluster_centers_)
#centers = np.array(model.cluster_centers_)
#plt.scatter(centers[:,0], centers[:,1], marker="x", color='r')
plt.show()