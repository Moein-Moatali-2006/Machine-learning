import numpy as np


class Perceptron:
    def __init__(self,learning_rate,epochs):
        self.w = np.random.rand(2,1)
        self.b = np.random.rand()
        self.learning_rate_w = learning_rate
        self.learning_rate_b = learning_rate
        self.epochs = epochs
        self.loss_history = [] # MSE

    def fit(self,X_train,Y_train):
        for j in range(self.epochs):
            loss = 0
            for i in range(X_train.shape[0]):
                x = X_train[i].reshape(1, -1)
                y = Y_train[i]
                y_pred = x @ self.w + self.b
                error = y - y_pred
                # update w and b
                self.w = self.w + self.learning_rate_w * (x.T * error)
                self.b = self.b + self.learning_rate_b * np.sum(error)
                loss += float(error ** 2)
            self.loss_history.append(loss)
    
    def predict(self,X_test):
        return X_test @ self.w + self.b

    def evaluate(self,X_test,Y_test):
        y_pred = self.predict(X_test)
        mse = np.mean((y_pred - Y_test)**2)
        return mse