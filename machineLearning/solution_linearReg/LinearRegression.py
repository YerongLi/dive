import numpy as np

class LinearRegression:
    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        tol = 1e-5
        prev_loss = 0
        for i in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias
            dw = (1/n_samples) * (np.dot(X.T, (y_pred - y)))
            db = (1/n_samples) * (np.sum(y_pred - y))
            self.weights = self.weights - (self.lr * dw)
            self.bias = self.bias - (self.lr * db)
            
            current_loss = np.mean(np.square(y_pred - y))
            
            if abs(current_loss - prev_loss) < tol:
                break
                
            prev_loss = current_loss
        
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias



#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
# import matplotlib.pyplot as plt
# from LinearRegression import LinearRegression


# In[2]:


n_samples = 1000
n_features = 10


# In[3]:


X, y = make_regression(n_samples=n_samples, n_features=n_features,
                       n_informative=5, noise=10, random_state=42)


# In[4]:


X_fit, X_val, y_fit, y_val = train_test_split(X, y, test_size=.2, random_state=1)


# In[5]:


# fig = plt.figure(figsize=(6,4))
# plt.scatter(X[:, 0], y, color="red", marker="o", s=5)
# plt.show()


# In[6]:


def mse(y, predictions):
    return np.mean(np.square(y - predictions))
# 99.49483120868547
# In[7]:


model = LinearRegression(lr=0.01)
model.fit(X_fit, y_fit)
train_predictions = model.predict(X_fit)


# In[8]:


print(mse(y_fit, train_predictions))
print('Groud Truth should be 99.49483120868547')



