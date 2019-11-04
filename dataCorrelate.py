'''
Mogamad Raa-iq Williams
Data Mining
'''

from numpy import corrcoef
from pylab import pcolor, colorbar, xticks, yticks
from numpy import arange
from pylab import show 
from dataImport import *

#Correlation
print("-----------")
print("Correlation")
print("-----------")
#Using numpy module corrcoef
corr = corrcoef(data.T) #.T used to give transpose
print(corr)
#Displaying correlation between data values
pcolor(corr)
colorbar()
xticks(arange(0.5,4.5), ['Recency', 'Frequency', 'Monetary', 'Time'], rotation=-20)
yticks(arange(0.5,4.5), ['Recency', 'Frequency', 'Monetary', 'Time'], rotation=-20)
show()
