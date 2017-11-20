import sys
print(sys.version)

import sklearn
sklearn.__version__

import numpy as np
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

X = data.data
X.shape # an array of each dimension (number of rows, number of columns)

noise = np.random.randn(X.shape[0],X.shape[0]) # artificially add some noise 569*569
X = np.hstack([X,noise]) # adding noise as features, to make the problem harder to solve
Y = data.target #label

from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

# please try out different C values
lr = LR(C=1.0) # create a model, set the parameters (hyperparameter)
lr.fit(X_train, Y_train) # train the model

lr.score(X_test, Y_test) # prediction performance, accuracy

from sklearn.metrics import precision_score,recall_score

precision = precision_score(Y_test, lr.predict(X_test),pos_label=1)
recall = recall_score(Y_test, lr.predict(X_test),pos_label=1)
print(precision)
print(recall)

lr.classes_

# TPR = TP/P
# FPR = FP/N
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(Y_test, lr.predict_proba(X_test)[:,1],pos_label=1)

%matplotlib inline
import matplotlib.pyplot as plt
plt.figure()
plt.plot(fpr, tpr, color='darkorange')
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Postive Rate, FPR')
plt.ylabel('True Positive Rate, TPR')
plt.title('Receiver operating characteristic example')
plt.show()