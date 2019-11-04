'''
Mogamad Raa-iq Williams
Data Mining
'''

from sklearn.decomposition import PCA
from dataImport import *
from pylab import plot,show

#Compression
print("-----------")
print("Compression")
print("-----------")
#Using pca module (Principal Component Analysis) to establish object
pca = PCA(n_components=2)
pcad = pca.fit_transform(data)

#Plot of principal components (PCs)
plot(pcad[target==1,0],pcad[target==1,1],'bo')
plot(pcad[target==2,0],pcad[target==2,1],'ro')
show()
#Determine how much information is stored in PCs
print("PCA Variance: ")
print(pca.explained_variance_ratio_)
#Determine information lost during transformation process
print("Information lost throughout transformation: ")
print(1-sum(pca.explained_variance_ratio_))
