import numpy as np


class LLS:
    def __init__(self):
        self.w = None  
    

    def fit(self, X, y):
        X = np.c_[np.ones(X.shape[0]), X]
        self.w = np.linalg.inv(X.T @ X) @ X.T @ y
    
    def predict(self, X):
        if self.w is None:
            raise ValueError("Model has not been fitted yet. Please call the 'fit' method first.")
        
        X = np.c_[np.ones(X.shape[0]), X] 
        return X @ self.w
