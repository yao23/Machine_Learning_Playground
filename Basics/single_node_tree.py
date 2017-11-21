# to demo, at a node (a certain training data), how to do the split

import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
%matplotlib inline

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

print "X: ", X[:10]
print "y: ", y[:10]
print "y values: ", np.unique(y)

from collections import Counter

a = [1,1,2,3,3,4,4,4,5,6,6,6]
# to find each elements' apperance

aCounter = Counter(a)
aCounter

# gini index =  sum(n_i/n * (1 - sum(pj**2)))

# n -- split --> (n1, n2)

def giniIndex(y1, y2):
    # y1 and y2 are the labels after the node split
    n1 = len(y1)
    n2 = len(y2)
    n = n1 + n2
    y1Counter = Counter(y1)
    y2Counter = Counter(y2)
    y1Ps = np.array([v/float(n1) for v in y1Counter.values()])
    y2Ps = np.array([v/float(n2) for v in y2Counter.values()])
    y1Gini = 1 - sum(y1Ps**2)
    y2Gini = 1 - sum(y2Ps**2)
    return float(n1)/(n)*y1Gini + float(n2)/(n)*y2Gini

# the original data's label is [1,1,1,1,0,0,0,0]
giniIndex([1,1,0,0],[1,1,0,0])

giniIndex([1,0,0,0],[1,1,1,0])

giniIndex([1,1,1,1],[0,0,0,0])

# should be implemented as a class, but here in order to demo easily
# trying to find how to split the data into two groups,
# such that each groups contain more pure data
bestFeature = -1 # the index in the X
bestCutVal = 0
bestGiniIndex = 1.
for j in np.arange(X.shape[1]): # iterate through all the features
    uniqueVals = np.unique(X[:,j])
    for val in uniqueVals: # iterate through all the possible cut values
        # now node splitting
        y1 = y[X[:,j]<val]
        y2 = y[X[:,j]>=val]
        temp = giniIndex(y1, y2) # compute the current gini index
        if(temp < bestGiniIndex ):
            bestGiniIndex = temp
            bestFeature = j
            bestCutVal = val

print "feature to use to split the node: ", bestFeature
print "best cut value: ", bestCutVal
print "gini index: ", bestGiniIndex

y1 = y[X[:,bestFeature]<bestCutVal]
y2 = y[X[:,bestFeature]>=bestCutVal]

Counter(y)

Counter(y1)

Counter(y2)