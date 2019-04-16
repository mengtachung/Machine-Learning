import pandas
from sklearn import svm 
#X = [[2, 0], [1, 1], [1.5, 1.5], [2,3]] 
#y = [0, 0, 0, 1]
X = [[2, 0], [1, 1], [2,3]] 
y = [0, 0, 1] 
clf = svm.SVC(kernel = 'linear') 
clf.fit(X, y)
#print (clf)

# get support vectors 
print ("support vectors=", clf.support_vectors_)

# get indices of support vectors 
#print ("indices of support vectors=", clf.support_)

# get number of support vectors for each class 
print ("# of support vectors for each class:", clf.n_support_)

## prediction
print("predicting (0.5, 0.5) =", clf.predict([[0.5, 0.5]]))
print("predicting (6, 6)=", clf.predict([[6, 6]]))

