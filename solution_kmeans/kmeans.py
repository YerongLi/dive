import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist

def k_means(X, K):
    centroids_history = []
    labels_history = []
    rand_index = np.random.choice(X.shape[0], K)
    centroids = X[rand_index]
    centroids_history.append(centroids)
    while True:
        labels = np.argmin(cdist(X, centroids), axis=1)
        labels_history.append(labels)
        new_centroids = np.array([X[labels == i].mean(axis=0)
                                  for i in range(K)])
        centroids_history.append(new_centroids)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    return centroids, labels, centroids_history, labels_history

# Load Iris dataset from sklearn
iris = load_iris()
X = iris.data

centroids, labels, centroids_history, labels_history = k_means(X, 3)

# Calculate Silhouette Score for PetalLengthCm and PetalWidthCm columns
silhouette_score_value = silhouette_score(X[:, [2, 3]], labels)
print("Silhouette Score:", silhouette_score_value)
