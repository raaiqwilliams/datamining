'''
Mogamad Raa-iq Williams
Data Mining
'''
from numpy.random import rand
from numpy import linspace, matrix
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from pylab import plot, show

#Regression
print("-----------")
print("Linear Regression")
print("-----------")
#Establish random variables
x = rand(40,1) #Explanatory variable
y = x*x*x+rand(40,1)/5 #Dependant variable

#Initialization of linear regression module
lr = LinearRegression()
lr.fit(x,y)

#Plotting and fitting LinearRegression to model
xx = linspace(0,1,40)
plot(x,y,'o',xx,lr.predict(matrix(xx).T),'--r')
show()

#Quantify the fit from linear model to original
print("Quantifying model fit to original data using mean squared error: ")
print(mean_squared_error(lr.predict(x),y))
