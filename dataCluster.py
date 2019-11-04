'''
Mogamad Raa-iq Williams
Data Mining
'''

from sklearn.cluster import KMeans
from sklearn.metrics import completeness_score, homogeneity_score
from pylab import plot, show, figure, subplot

from dataImport import *
from dataClassify import *

#Clustering
print("-----------")
print("Clustering")
print("-----------")
km = KMeans(n_clusters=2, init='random') # initialization
km.fit(data) # actual execution

#Predict
c = km.predict(data)

#Completeness score
print("Completeness score: ")
print(completeness_score(t,c))
#Homogeneity score
print("Homogeneity score: ")
print(homogeneity_score(t,c))

#Plotting figure with real classes
figure()
plot(data[t==1,0],data[t==1,2],'mo')
plot(data[t==2,0],data[t==2,2],'bo')
show()
