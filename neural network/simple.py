import numpy as np
import matplotlib.pylab as plt

X = np.array([1,2])
X.shape
W = np.array([[1,3,5],[2,4,6]])
W.shape

Y = np.dot(X,W)
print(Y)