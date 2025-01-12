import numpy 


class KNN:
    def __init__(self,k):
        self.k = k


    def fit(self,X_train,Y_train):
        self.X_train = X_train
        self.Y_train = Y_train

    def euclidean_distance(self,x1,x2):
        return numpy.sqrt(numpy.sum((x1 - x2) ** 2))
    
    def predict(self,X_test):
        Y_pred = []
        for x in X_test:
            distances = []
            for x_train in self.X_train:
                distance = self.euclidean_distance(x_train,x)
                distances.append(distance)
            
            nearest_neighbors = numpy.argsort(distances)[:self.k]
            nearest_labels = self.Y_train[nearest_neighbors]
            result = numpy.bincount(nearest_labels).argmax()
            Y_pred.append(result)
        
        return Y_pred

    def evaluate(self,X_test,Y_test):
        Y_pred = self.predict(X_test)
        correct = sum(y_pred == y_true for y_pred,y_true in zip(Y_pred, Y_test))
        accuracy = correct / len(Y_test)
        return accuracy