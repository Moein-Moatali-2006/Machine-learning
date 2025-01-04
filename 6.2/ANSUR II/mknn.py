import numpy as np

class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, Y):
        self.X_train = X
        self.Y_train = Y

    def euclidean(self, p1, p2):
        return np.sqrt(np.sum((p1 - p2) ** 2))

    def predict(self, X):
        Y = []
        for x in X:
            distances = []
            for x_train in self.X_train:
                number = self.euclidean(x, x_train)
                distances.append(number)
            
            nearest_neighbors = np.argsort(distances)[:self.k]
            result = np.bincount(self.Y_train[nearest_neighbors])
            y = np.argmax(result)
            Y.append(y)
        
        return np.array(Y)  
    
    def score(self, X, Y):
        y_pred = self.predict(X)
        accuracy = np.sum(y_pred == Y) / len(Y)
        return accuracy
