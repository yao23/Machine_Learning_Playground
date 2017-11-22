# support vector machine

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
%matplotlib inline

# Kernel: Replace the dot product of data points, np.dot(X.T,X), with another function so that it is equivalent to
# projecting the data points to a higher dimension space (through nonliner transformation).
# In such way, we can deal with nonlinear problem.

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    # create a meshgrid
    # find the coordinates for all the points with the region (x_min, x_max) (y_min, y_max)
    return xx, yy


def plot_contours(clf, xx, yy, **params):
    # clf classifier
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = plt.contourf(xx, yy, Z, **params)
    return out

def myPlot(clf, xx, yy, X0, X1, title):
    plot_contours(clf, xx, yy,
                  cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xticks(())
    plt.yticks(())
    plt.title(title)
    plt.show()


iris = datasets.load_iris()
# Take the first two features. We could avoid this by using a two-dim dataset
X = iris.data[:, :2]
y = iris.target

C = 1  # SVM regularization parameter
svm_linear = svm.SVC(kernel='linear', C=C).fit(X, y)
svm_rbf = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
svm_poly = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)


# title for the plots
titles = ('SVC with linear kernel',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel')

X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)

myPlot(svm_linear, xx, yy, X0, X1, "linear SVM")

myPlot(svm_rbf, xx, yy, X0, X1, "SVM with RBF kernel")

myPlot(svm_poly, xx, yy, X0, X1, "SVM with polynomial (degree 3) kernel")


svm_rbf = svm.SVC(kernel='rbf', gamma=7, C=100).fit(X, y)
myPlot(svm_rbf, xx, yy, X0, X1, "SVM with RBF kernel, overfitting")


# Using SVM to do image recognition
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()

images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)


# training and prediction

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
print n_samples
print data[:2]


X = data/16.
Y = digits.target


from sklearn.model_selection import GridSearchCV
# cross-validation, find the best classifier
Cs = np.logspace(-6, -1, 10)
kernels = ["linear","rbf","poly"]
degrees = [2,3,4]
gammas = [0.001,0.01,0.1,1,2,5]
modelCV = GridSearchCV(estimator=svm.SVC(),
                   param_grid=dict(C=Cs,kernel=kernels,degree=degrees,
                                   gamma=gammas),n_jobs=-1)
modelCV.fit(X[:n_samples // 2], Y[:n_samples // 2]) #use half the data for training

classifier = modelCV.best_estimator_
print(classifier)


# Now predict the value of the digit on the second half:
# for test
expected = Y[n_samples // 2:]
predicted = classifier.predict(X[n_samples // 2:])

print("Classification report %s\n" % (metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()