import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


class Perceptron:
    def __init__(self, learning_rate, input_length):
        self.learning_rate = learning_rate
        self.weights = np.random.rand(input_length)
        self.b = np.random.rand(1)
        self.train_losses = []
        self.test_losses = []
        self.train_accuracies = []
        self.test_accuracies = []
    
    def activation(self, x, function):
        if function == "sigmoid":
            return 1 / (1 + np.exp(-x))
        elif function == "linear":
            return x
        elif function == "tanh":
            return np.tanh(x)
        elif function == "relu":
            return np.maximum(0, x)
        elif function == "SiLU":
            return x / (1 + np.exp(-x))
        else:
            raise Exception("Error: give me a valid function!")

    def fit(self, X_train, Y_train, X_test, Y_test, epochs, activation_function="sigmoid"):
        for _ in range(epochs):
            # Training 
            for x, y in zip(X_train, Y_train):
                y_pred = self.activation(np.dot(x, self.weights) + self.b, activation_function)
                error = y - y_pred
                self.weights += self.learning_rate * error * x
                self.b += self.learning_rate * error
            
            # Calculating train loss and accuracy
            Y_pred_train = self.predict(X_train, activation_function)
            train_loss = self.calculate_loss(Y_train, Y_pred_train, "mse")
            train_accuracy = self.calculate_accuracy(Y_train, Y_pred_train)
            self.train_losses.append(train_loss)
            self.train_accuracies.append(train_accuracy)
            
            # Calculating test loss and accuracy
            Y_pred_test = self.predict(X_test, activation_function)
            test_loss = self.calculate_loss(Y_test, Y_pred_test, "mse")
            test_accuracy = self.calculate_accuracy(Y_test, Y_pred_test)
            self.test_losses.append(test_loss)
            self.test_accuracies.append(test_accuracy)

    def predict(self, X_test, activation_function="sigmoid"):
        Y_pred = [self.activation(np.dot(x, self.weights) + self.b, activation_function) for x in X_test]
        return np.array(Y_pred)
    
    def calculate_loss(self, Y_true, Y_pred, metric):
        if metric == "mae":
            return np.mean(np.abs(Y_true - Y_pred))
        elif metric == "mse":
            return np.mean((Y_true - Y_pred) ** 2)
        elif metric == "rmse":
            return np.sqrt(np.mean((Y_true - Y_pred) ** 2))
        else:
            raise Exception("Error: give me a valid metric!")
    
    def calculate_accuracy(self, Y_true, Y_pred):
        correct = np.sum((Y_pred >= 0.5) == Y_true)
        return correct / len(Y_true)
    
    def evaluate(self, X_test, Y_test, metric="mse"):
        Y_pred = self.predict(X_test)
        loss = self.calculate_loss(Y_test, Y_pred, metric)
        accuracy = self.calculate_accuracy(Y_test, Y_pred)
        return loss, accuracy

    def Calculate_confusion_matrix(self, Y_test, Y_pred):
        Y_pred_class = (Y_pred >= 0.5).astype(int)  
        cm = confusion_matrix(Y_test, Y_pred_class)
        return cm
    
    def show_plot_losses(self):
        plt.plot(range(len(self.train_losses)), self.train_losses, label="Train Loss")
        plt.plot(range(len(self.test_losses)), self.test_losses, label="Test Loss")
        plt.title("Loss and Epochs")
        plt.xlabel("Epochs")
        plt.ylabel("Loss")
        plt.legend()
        plt.show()

    def show_plot_accuracy(self):
        plt.plot(range(len(self.train_accuracies)), self.train_accuracies, label="Train Accuracy")
        plt.plot(range(len(self.test_accuracies)), self.test_accuracies, label="Test Accuracy")
        plt.title("Accuracy and Epochs")
        plt.xlabel("Epochs")
        plt.ylabel("Accuracy")
        plt.legend()
        plt.show()


    def plot_confusion_matrix(self, cm):
        fig, ax = plt.subplots(figsize=(6,6))
        cax = ax.matshow(cm, cmap="Blues")
        fig.colorbar(cax)
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("True")
        plt.xticks([0, 1], ["Class 0", "Class 1"])
        plt.yticks([0, 1], ["Class 0", "Class 1"])
        plt.show()