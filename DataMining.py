'''
Mogamad Raa-iq Williams
Data Mining
'''
#A data mining exercise on data regarding a Blood Tranfusion Service Center (dataset found at https://archive.ics.uci.edu/ml/datasets/Blood+Transfusion+Service+Center)

#Data taken from the Blood Transfusion Service Center in Hsin-Chu City in Taiwan -- this is a classification problem.
#To demonstrate the RFMTC marketing model (a modified version of RFM),
#this study adopted the donor database of Blood Transfusion Service Center in Hsin-Chu City in Taiwan.
#The center passes their blood transfusion service bus to one university in Hsin-Chu City to gather blood donated about every three months.
#To build an FRMTC model, we selected 748 donors at random from the donor database.

### Attribute Information
#* V1: Recency - months since last donation
#* V2: Frequency - total number of donation
#* V3: Monetary - total blood donated in c.c.
#* V4: Time - months since first donation), and a binary variable representing whether he/she donated blood in March 2007 (1 stand for donating blood; 0 stands for not donating blood).

#The target attribute is a binary variable representing whether he/she donated blood in March 2007 (2 stands for donating blood; 1 stands for not donating blood).

import dataImport, dataVisualize, dataClassify, dataCluster, dataRegress, dataCorrelate, dataCompress



