# use random forest for breast cancer data
# number of trees
# cross-validation, and oob (out of bagging error)
# feature importance

import numpy as np

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

X = data.data
Y = data.target
print(X.shape)
# to demonstrate the case, when there are a lot of noisy features
noise = np.random.randn(X.shape[0], X.shape[0]) # noise from normal distribution
X = np.hstack([X,noise])
print X.shape
print Y[:2]

# demo resample data
Xdemo = X[:10]
Xdemo_resample_index = np.random.choice([i for i in range(10)], 10)
Xdemo_resample = X[Xdemo_resample_index]
print "indices after resample: ", Xdemo_resample_index
print "resampled training data: ", Xdemo_resample

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

# experiment 1, prediction power and number of trees
from sklearn.ensemble import RandomForestClassifier as RFC
scores = []
n_trees_list = [1,2,5,10,20,50,80]
for n_trees in n_trees_list:
    # build a model using different number of trees
    model = RFC(n_estimators = n_trees)
    # now train the model
    model.fit(X_train, Y_train)
    scores.append(model.score(X_test, Y_test))

import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(n_trees_list, scores)
plt.xlabel("number of trees")
plt.ylabel("prediction accuracy")
plt.show()

# in principle, the more trees, the better

# experiment 1, prediction power and number of trees
from sklearn.ensemble import RandomForestClassifier as RFC

scores = []
n_trees_list = [1, 2, 5, 10, 20, 50, 80, 100, 200, 500]
for n_trees in n_trees_list:
    model = RFC(n_estimators=n_trees, max_features=3)
    model.fit(X_train, Y_train)
    scores.append(model.score(X_test, Y_test))

plt.plot(n_trees_list, scores)
plt.xlabel("number of trees")
plt.ylabel("prediction accuracy")
plt.show()

# feature importance
model = RFC(50)
model.fit(X_train, Y_train)

model.feature_importances_

data.feature_names

zippped_featureImg = zip(data.feature_names, model.feature_importances_)
zippped_featureImg

print sorted(zippped_featureImg, key=lambda x: x[1], reverse=True)

index_most_important = list(data.feature_names).index("worst radius")

plt.plot(X[:, index_most_important], Y, 'ro')
plt.xlabel('worst radius')
plt.ylabel('response')
plt.ylim(-0.5,1.5)
plt.show()

index_least_important = list(data.feature_names).index('mean symmetry')
plt.plot(X[:, index_least_important], Y, 'ro')
plt.xlabel('worst radius')
plt.ylabel('response')
plt.ylim(-0.5,1.5)
plt.show()

# out of bag score, replace cross validation
import time
model = RFC(50, oob_score=True)

start = time.clock()
model.fit(X,Y)
print(model.oob_score_) # also to estimate the test score
print "Running time (sec): ", (time.clock() - start)

from sklearn.model_selection import cross_val_score
start = time.clock()
print cross_val_score(RFC(50), X, Y, cv=5).mean()
print "Running time (sec): ", (time.clock() - start)

# 0.947275922671
# Running time (sec):  0.697596
# 0.947395151982
# Running time (sec):  2.425713