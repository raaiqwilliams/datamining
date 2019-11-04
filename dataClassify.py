'''
Mogamad Raa-iq Williams
Data Mining
'''
from numpy import zeros
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from dataImport import *

#Classification
print("-----------")
print("Classification")
print("-----------")
#Converting target array into integers for convenience 
t = zeros(len(target))
t[target == 1] = 1
t[target == 2] = 2

#Instantiation and training of classifier
classifier = GaussianNB()
classifier.fit(data,t) #training on dataset

#Taking 40% of dataset as test values, retraining classifier and printing accuracy
train, test, t_train, t_test = train_test_split(data, t, test_size = 0.4, random_state = 0)
classifier.fit(train, t_train)
print("Accuracy of prediction using 40% of dataset as test values: ")
print(classifier.score(test,t_test))

#Below are a few ways of testing classifier that was established
'''
#Testing predict with sample
print("Classification using predict method: ")
print(classifier.predict(data[[0]]))

#Estimating performance of classifier once more by means of a confusion matrix
print("Confusion matrix to estimate performance of classifier: ")
print(confusion_matrix(classifier.predict(test),t_test))

'''

#Finally printing the summary of classifiers prediction accuracy and performance
print("Complete report of classifier performance: ")
print(classification_report(classifier.predict(test), t_test, target_names=['1','2']))
