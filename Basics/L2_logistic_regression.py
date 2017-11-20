#Implement logistic regression with L2 norm

# y_i(1-y_i_hat)-(1-y_i)y_i_hat

# y_i-y_i_hat, y_i=1 or 0

# the gradient of CE is just (y_i-y_i_hat)*x

import numpy as np

class twoClassLogisticRegression():
    def __init__(self, lbda=1., tol=0.001, alpha=0.1):
        # __init__ is a function (constructor) called when somebody write
        # myModel = twoClassLogisticRegression(lbda=0.5) (1/C)
        self.lbda = lbda  # regularizer penalty
        self.tol = tol  # tolerance
        self.alpha = alpha  # learning rate

    def logistic(self, u):
        # u is the linear function of features
        # u = w0 + w1*x1 + w2*x2 ...
        return 1. / (1. + np.exp(-u))

    def fit(self, X, Y):
        # model training
        # X is the design matrix with the shape N by p
        # y is the response as a 1-d array e.g. [0,1,1,0,1...]
        N = X.shape[0]
        p = X.shape[1]
        self._class = np.unique(Y)  # list all class labels e.g. ["A","B"]
        assert (len(self._class) == 2)
        self._class.sort()
        self._class = list(self._class)
        print "class labels: ", self._class
        Y_label = np.array([self._class.index(y) for y in Y])  # now Y_label is 1 or 0 for sure
        Y_label = Y_label[:, np.newaxis]  # transform Y_label to be a column vector

        # Y_label is column vector of 0 or 1

        # initialize weights, also use a bias constant, u = w0 + w1x1 + w2x2 ...
        w_old = np.random.randn(p, 1)  # w1...wp, normal distribution
        w0_old = np.random.randn(1)  # w0, normal distribution

        while (True):
            Y_hat = self.logistic(np.dot(X, w_old) + w0_old)  # make prediction
            g_w = -((Y_label - Y_hat) * X).mean(axis=0)[:, np.newaxis] + self.lbda * w_old
            # [:, np.newaxis] to make 1-d vector to 2-d column vector
            g_w0 = -(Y_label - Y_hat).mean(axis=0)
            # steepest gradient descent
            w_new = w_old - self.alpha * g_w
            w0_new = w0_old - self.alpha * g_w0
            if (((w_old - w_new) ** 2).sum() < self.tol):
                print "the algorithm has converged"
                break
            w_old = w_new
            w0_old = w0_new

        self.w = w_new
        self.w0 = w0_new

    def predict_prob(self, X):
        return self.logistic(np.dot(X, self.w) + self.w0)

    def predict(self, X):
        probs = self.predict_prob(X)
        labels = [1 if x > 0.5 else 0 for x in probs]  # using list comprehension, threshold set to be 0.5
        return [self._class[label] for label in labels]

    def score(self, X, Y):
        Y_pred = self.predict(X)
        accuracy = np.mean(Y == Y_pred)
        return accuracy

model = twoClassLogisticRegression() # compare to sklearn logisticRegression

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = data.data
Y = data.target
print(X.shape)
print(Y.shape)
print(X.mean(axis=0)) # compute every feature's mean


# preprocessing standardization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X) # standardization
print(X.mean(axis=0))

model.fit(X, Y)

model.score(X, Y) #training accuracy