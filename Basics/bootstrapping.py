# How to estimate the distribution of a mean of 1000 data sampled from a normal distribution
# suppose X~N(0,1), what is the mean and variance of X1 + X2 + X3 + X4 + .. X1000?

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

X1 = np.random.randn(1) # from N(0,1) sample one data
X1

Xs = np.zeros(1000) # an empty list to contain the numbers we generated
for i in range(len(Xs)):
    Xs[i] = np.random.randn(1)
Xs.shape

plt.hist(Xs)

# a better way
Xs = np.random.randn(1000)
Xs.shape

# if X's are random variables (they are independent, indistinct distributed, iid)
# their mean is also random variable, what is the mean and variance then?

X_mean = Xs.mean()
X_mean # we only have one value, how do we know its mean?

# well what we can do is to sample multiple batches,
X_means = np.zeros(100)
for i in range(len(X_means)):
    Xs = np.random.randn(1000)
    X_means[i] = Xs.mean()

X_means

plt.hist(X_means)

print "the mean of X: ", np.random.randn(10000).mean()
print "the mean of mean(X1...X1000): ",X_means.mean()
print "the variance (standard deviation) of X: ",np.random.randn(10000).std()**2
print "the variance of mean(X1...X1000): ",X_means.std()**2

# that is what we already know from math: var(X_mean) = var(X)/N

# how do we do it if we only has one sample of data. Say we only have one Xs
# we simulate the distribution of X by resampling the Xs
X_means_bootstrapping = np.zeros(100)
for i in range(len(X_means)):
    Xs_resample = np.random.choice(Xs, len(Xs))
    # bootstrapping, resample a sample data, to simulate the real distribution
    # generally speaking, resampling will use the same size as the original data
    X_means_bootstrapping[i] = Xs_resample.mean()

plt.hist(X_means_bootstrapping)

print "the mean of X: ", np.random.randn(10000).mean()
print "the mean of mean(X1...X100): ",X_means_bootstrapping.mean()
print "the variance (standard deviation) of X: ",np.random.randn(10000).std()**2
print "the variance of mean(X1...X100): ",X_means_bootstrapping.std()**2

a = [1,2,3,4,5]
np.random.choice(a,5)
# array([4, 3, 3, 4, 4])

np.random.choice(a,5, replace=False)
array([2, 3, 4, 5, 1])