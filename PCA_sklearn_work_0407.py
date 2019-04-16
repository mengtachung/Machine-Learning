import numpy as np
import pandas as pd    #### error message without this
from sklearn.decomposition import PCA
A = np.array([[1, 1],
       [1, 3],
       [2, 3],
       [4, 4],
       [2, 4]])
pca = PCA(n_components=2)
pf =pca.fit_transform(A)

print ("eigenvectors=\n", pca.components_)
print ("eigenvalues=\n", pca.explained_variance_)
print ("components =\n", pf)
print ("principle component =\n", pf[:, 0])
#print (pca.explained_variance_ratio_)
