
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv("weight-height.csv")

X = data["Height"].values
Y = data["Weight"].values

X_train , X_test , Y_train , Y_test = train_test_split(X,Y,shuffle=True,test_size=0.99)

X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)
Y_train = Y_train.reshape(-1,1)
Y_test = Y_test.reshape(-1,1)

fig , (ax1,ax2) = plt.subplots(1,2)

losses = []

# Trading
w = np.random.rand(1,1)
b = np.random.rand(1,1)
learning_rate_w = 0.0001
learning_rate_b = 0.01

epochs = 20
for j in range(epochs):
    for i in range(X_train.shape[0]):
        
        x = X_train[i]
        y = Y_train[i]
        y_pred = x * w + b
        error = y - y_pred 

        # SGD update 
        w = w + (learning_rate_w * error * x)
        b = b + (learning_rate_b * error)
        
        #mae
        loss = np.mean(np.abs(error))
        losses.append(loss)

        Y_pred = X_train * w + b
        ax1.clear()
        ax1.scatter(X_train,Y_train,color="blue")
        ax1.plot(X_train,Y_pred,color="red")
        plt.pause(0.01)

        ax2.clear()
        ax2.plot(losses)
        plt.pause(0.01)