import numpy as np

def train_test_split(X,Y,train_size=0.2,random=True):
    if len(X) != len(Y):
        raise ValueError("The number of X and Y elements must be equal!")
    
    n_train = int(len(X) * train_size)

    if random:
        indices = np.random.permutation(len(X))
    else:
        indices = np.arange(len(X))

    train_indices = indices[:n_train]
    test_indices = indices[n_train:]

    X_train, X_test = X[train_indices], X[test_indices]
    Y_train, Y_test = Y[train_indices], Y[test_indices]
    
    return X_train,X_test,Y_train,Y_test



x = np.array([1,2,3,4,5,6,7,8,9,10]) 
y = np.array([5,10,15,20,25,30,35,40,45,50]) 
X_train , X_test , Y_train , Y_test = train_test_split(x,y,train_size=0.4,random=True)

print(X_train)
print(Y_train)
print(X_test)
print(Y_test)

