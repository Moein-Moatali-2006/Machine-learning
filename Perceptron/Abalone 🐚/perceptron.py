import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate, epochs):
        self.w = np.random.rand()
        self.b = np.random.rand()

        self.learning_rate_w = learning_rate
        self.learning_rate_b = learning_rate
        self.epochs = epochs
        self.size = input_size
        self.loss_history = []


    def fit(self, X_train, Y_train):
        for j in range(self.epochs):
            total_loss = 0
            for i in range(X_train.shape[0]):
                x = X_train[i]
                y = Y_train[i]
                y_pred = x * self.w + self.b
                error = y - y_pred

                # SGD update
                self.w = self.w + (self.learning_rate_w * error * x)
                self.b = self.b + (self.learning_rate_b * error)
                # loss
                total_loss += error ** 2
            self.loss_history.append(total_loss / len(X_train))

    def predict(self, X_test):
        return X_test * self.w + self.b

    def evaluate(self, X_test, Y_test):
        y_pred = self.predict(X_test)
        # Mean Squared Error
        mse = np.mean((Y_test - y_pred)**2)
        return mse