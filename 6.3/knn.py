import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class KNN:
    def __init__(self, k):
        self.k = k
    
    # training
    def fit(self, X, Y):
        self.X_train = X
        self.Y_train = Y
    
    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))
    
    def predict(self, X):
        Y = []
        for x in X:
            distances = []
            for x_train in self.X_train:
                d = self.euclidean_distance(x, x_train)
                distances.append(d)

            nearest_neighbors = np.argsort(distances)[:self.k]
            result = np.bincount(self.Y_train[nearest_neighbors])
            y = np.argmax(result)
            Y.append(y)

        return Y

    def evaluate(self, X, Y):
        y_pred = self.predict(X)
        accuracy = np.sum(y_pred == Y) / len(Y)
        return accuracy


if __name__ == "__main__":
    iris = load_iris()
    X = iris.data
    Y = iris.target

    X_train, X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2)

    knn_moein = KNN(k=3)
    knn_moein.fit(X_train,Y_train)
    accuracy = knn_moein.evaluate(X_test,Y_test)
    print("accuracy:",accuracy)

    knn_sklearn = KNeighborsClassifier(n_neighbors=3)
    knn_sklearn.fit(X_train,Y_train)
    accuracy = knn_sklearn.score(X_test,Y_test)
    print("accuracy:",accuracy)
