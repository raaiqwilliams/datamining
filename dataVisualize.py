'''
Mogamad Raa-iq Williams
Data Mining
'''

from pylab import plot, show, figure, subplot, hist, xlim
from dataImport import *

#Visualization
print("-----------")
print("Visualization")
print("-----------")

#Printing test visualization of Frequency(V2) with Time(V4)
#hence determining total number of donations considering total time since first donation
plot(data[target == 1,1],data[target==1,3],'bo')
plot(data[target == 2,1],data[target==2,3],'ro')
show()

#Plotting and printing of histograms
xmin = min(data[:,1])
xmax = max(data[:,1])
figure()

subplot(211) # distribution of the first class
hist(data[target == 1,1],color='b',alpha=.7)
xlim(xmin,xmax)
subplot(212) # distribution of the second class
hist(data[target == 2,1],color='r',alpha=.7)
xlim(xmin,xmax)
show()
