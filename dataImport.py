'''
Mogamad Raa-iq Williams
Data Mining
'''
from numpy import genfromtxt, zeros

#Importing
print("-----------")
print("Importing")
print("-----------")

#Generate type appropiate datatype to store columns 1 - 4 and printing
data = genfromtxt('transfusion.csv', delimiter=',', usecols=(0,1,2,3), encoding='utf-8', dtype='int64',skip_header=1)
print("Blood donation data: ")
print(data[:10])

#Generate type appropiate datatype to store column 5 in, and printing
target = genfromtxt('transfusion.csv', delimiter=',', usecols=(4), encoding='utf-8',dtype='int64', skip_header=1)
print("Class data: ")
print(target[:10])

#Printing set for Class (Either 1 or 2)
print("Set of target array values (Class): ")
print(set(target))
set(['1','2'])
