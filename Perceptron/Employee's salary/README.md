# Employee's salary 
Make a linear dataset using scikit-learn library.\
```python
from sklearn.datasets import make_regression
```
Split data to train and test datasets.
Implement the perceptron algorithm as a class.
```python
class Perceptron:
    def __init__(self, input_size, lr, epochs):
        self.w = ...
        self.b = ...
        ...

    def fit(self, X_train, Y_train):
        ...

    def predict(self, X_test):
        ...

    def evaluate(self, X_test, Y_test):
        ...
```
Fit your model on the employee's salary dataset.\
Plot data graph and loss graph as 2 subplots in 1 window.\
Change hyperparameters for get best result.