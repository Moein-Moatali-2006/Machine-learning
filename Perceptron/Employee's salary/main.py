import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split


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


X,Y = make_regression(n_samples=200,n_features=1,noise=10,random_state=42)
X_train , X_test , Y_train , Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

model = Perceptron(1,learning_rate=0.01,epochs=50)
model.fit(X_train,Y_train)

X_line = np.linspace(X.min(), X.max(), 100)  
Y_line = model.predict(X_line.reshape(-1, 1))

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].scatter(X_train, Y_train, color='blue', label='Actual Data')
axes[0].plot(X_line, Y_line, color='red', linewidth=2, label='Model Prediction')
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].set_title("Regression Line vs Actual Data")
axes[0].legend()

axes[1].plot(range(len(model.loss_history)), model.loss_history, color='green', linewidth=2)
axes[1].set_xlabel("Epochs")
axes[1].set_ylabel("Mean Squared Error (MSE)")
axes[1].set_title("Loss Reduction over Epochs")

plt.tight_layout() 
plt.show()

