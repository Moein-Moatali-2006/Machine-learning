import numpy as np


class Perceptron:
    def __init__(self,learning_rate,epochs):
        self.epochs = epochs
        self.w = np.random.rand()
        self.b = np.random.rand()
        self.learning_rate_w = learning_rate
        self.learning_rate_b = learning_rate
        self.loss_history = []

    def fit(self,X_train,Y_train):
        for j in range(self.epochs):
            loss = []
            for i in range(X_train.shape[0]):
                x = X_train[i]
                y = Y_train[i]
                y_pred = x * self.w + self.b
                error = y_pred - y
                # update SGD
                self.w = self.w + (x * self.learning_rate_w * error)
                self.b = self.b + (self.learning_rate_b * error)


    def predict(self,X_test):
        ...

    def evaluate(self,X_test,Y_test):
        ...