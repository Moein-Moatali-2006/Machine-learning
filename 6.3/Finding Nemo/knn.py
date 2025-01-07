import numpy as np
import cv2

class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, Y):
        self.X_train = X
        self.Y_train = Y

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predict(self, X_list):
        Y_list =[]
        for x in X_list:
            distances = []
            for x_train in self.X_train :
                distance = self.euclidean_distance(x,x_train)
                distances.append(distance)
            
            nearest_neighbors = np.argsort(distances)[:self.k]
            result = np.bincount(self.Y_train[nearest_neighbors])
            y = np.argmax(result) 

            Y_list.append(y)
        return Y_list

    def evaluate(self, X, Y):
        y_pred = self.predict(X)
        accuracy = np.sum(y_pred == Y) / len(Y)
        return accuracy
