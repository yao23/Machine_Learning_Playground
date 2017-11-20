import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import metrics, cross_validation
from sklearn.linear_model import LogisticRegression as logreg
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

# read in the data
# the data format is "dataframe"
data = pd.read_csv("training.csv")
#data.head()
len(data.index) # number of data (cars)

data.info()

# drop records with NAs for selected features and some inrelevant features
data2 = data.dropna(axis =0, how = 'any', subset = ['Color','Transmission','Nationality','Size','TopThreeAmericanName','MMRAcquisitionAuctionAveragePrice','MMRAcquisitionAuctionCleanPrice','MMRAcquisitionRetailAveragePrice',
'MMRAcquisitonRetailCleanPrice', 'MMRCurrentAuctionAveragePrice', 'MMRCurrentAuctionCleanPrice',
'MMRCurrentRetailAveragePrice','MMRCurrentRetailCleanPrice'])
len(data2.index)

# data visualization
# The purpose here is to check the variances of the features with categorical values, so that categories
# with small counts can be grouped together
%matplotlib inline

# check the response distribution
# histogram of isBadBuy
data2.IsBadBuy.hist()
plt.title('Histogram of IsBadBuy')
plt.xlabel('')
plt.ylabel('Frequency')

data2.Make.value_counts().plot(kind='bar')

def recategorize(data,columnname):
    # only when a feature shared by more than 5% of the totally record, we will retain it
    counts = data[columnname].value_counts()
    nameSet = set(counts[counts>= 0.01*len(data.index)].index.values)
    # at least 5% of all the data
    data.loc[:,columnname] = data[columnname].apply(lambda x:'OTHER'if x not in nameSet else x)
    return data

data2 = recategorize(data2, 'Make')
data2.Make.value_counts().plot(kind='bar')

data2 = recategorize(data2, 'Color')
data2.Color.value_counts().plot(kind='bar')

data.Transmission.value_counts().plot(kind='bar')

data.Nationality.value_counts().plot(kind='bar')

data.Size.value_counts().plot(kind='bar')

data.TopThreeAmericanName .value_counts().plot(kind='bar')

data2 = recategorize(data2, 'VNST')
data2.VNST.value_counts().plot(kind='bar')

data2.info()

data2_cleaned = data2.drop(["RefId", "PurchDate","VehYear", "WheelTypeID","BYRNO","VNZIP1","PRIMEUNIT","AUCGUART"],axis=1)
data2_cleaned.info()

# generate dummy variables for categorical data
dataFinal = pd.get_dummies(data2_cleaned)
len(list(dataFinal))

dataFinal.head()

Y = dataFinal.loc[:,"IsBadBuy"]
X = dataFinal.drop("IsBadBuy",1)

X.head()

from sklearn.preprocessing import StandardScaler as SC
sc = SC()
Xnew = sc.fit_transform(X)

Xnew[:5]