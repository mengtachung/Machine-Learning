import numpy as np
from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig

##### Data: 2 variables; 5 observations; len(X)=5
X = np.array([[1, 1],
      [1, 3],
      [2, 3],
      [4, 4],
      [2, 4]])
######################
#X = np.array([[2.5, 2.4],
#      [0.5, 0.7],
#      [2.2, 2.9],
#      [1.9, 2.2],
#      [3.1, 3.0],
#      [2.3, 2.7],
#      [2.0, 1.6],
#      [1.0, 1.1],
#      [1.5, 1.6],
#      [1.1, 0.9]])
print("data=\n", X)    #print(X.T) #### X.T = transpose (X)

# calculate the mean of each column
M = mean(X.T, axis=1)
#print(M)

# center columns by subtracting column means
C = X - M
#print(C)

# calculate covariance matrix of centered matrix
#V = (1/len(X-1))*np.dot(C.T, C)    #### divided by 4
#Y = np.array([ [-1, -1, 0, 2, 0], [-2, 0, 0, 1, 1] ])
#print( "cov Y", np.cov(Y) ) #### divided by 4
V = (1/len(X))*np.dot(C.T, C)    #### divided by 5
print("Covariance matrix=\n", V)

# eigendecomposition of covariance matrix
values, vectors = eig(V)
print("eigenvectors=\n", vectors)
print("eigenvalues=\n", values)

# project data
#P = vectors.T.dot(C.T)
P = np.dot(vectors.T, C.T)
print ("Components (centered) =\n", np.round(P, 3))
#print("Principle Component = ", P[0, :])    #### descending order
#print("Principle Component=\n",-np.sort(-P[0, :]))  #### ascending order
#print("Second Component=\n",-np.sort(-P[1, :]))  #### ascending order
P_ori =  np.dot(vectors.T, X.T)
#print ("Components (original scale) =\n", np.round(P_ori, 3))
