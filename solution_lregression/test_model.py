#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from LinearRegression import LinearRegression


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
exit()


# In[9]:


y_pred_train = model.predict(X_fit)

fig = plt.figure(figsize=(6,4))
plt.scatter(y_fit, y_pred_train, color="blue", s=5)
plt.plot([min(y), max(y)], [min(y), max(y)], color="red", linewidth=2)
plt.xlabel("True values")
plt.ylabel("Predicted train values")
plt.show()


# In[10]:


y_pred_val = model.predict(X_val)

fig = plt.figure(figsize=(6,4))
plt.scatter(y_val, y_pred_val, color="green", s=5)
plt.plot([min(y), max(y)], [min(y), max(y)], color="red", linewidth=2)
plt.xlabel("True values")
plt.ylabel("Predicted validation values")
plt.show()

