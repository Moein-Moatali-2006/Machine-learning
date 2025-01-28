import  numpy as np
from numpy.linalg import inv


class LinearLeastSquare:
    def __init__(self):
        pass

    def fit(self,X_train,Y_train):
        self.w = inv(X_train.T @ X_train) @ X_train @ Y_train
    
    def predict(self,X_test):
        Y_pred = self.w @ X_test
        return Y_pred
    
    def evaluate(self,Y_test,Y_pred,metric):
        
        if metric == "mae":
            loss = np.sum(np.abs(Y_test - Y_pred)) / len(Y_test)
        elif metric == "mse":
            loss = np.sum((Y_test-Y_pred)**2) / len(Y_test)
        elif metric == "rmse":
            loss = np.sqrt(np.sum((Y_test - Y_pred)**2) / len(Y_test))
        return loss