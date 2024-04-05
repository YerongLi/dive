from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from typing import List
import numpy as np

# Functions for boosting algorithm
def bootsample(n: int) -> List[int]:
    """
    Perform sampling with replacement n times and return the indices.
    """
    return np.random.choice(n, size=n, replace=True)

def fit(classifiers: List[object], x, y) -> None:
    """
    Train the boosting model with given classifiers.
    """
    # Initialize weights
    weights = np.ones(len(y)) / len(y)
    
    for clf in classifiers:
        # Use bootstrapped indices to create a new training set
        indices = bootsample(len(y))
        x_sampled, y_sampled = x[indices], y[indices]
        
        # Train the classifier with weights
        clf.fit(x_sampled, y_sampled, sample_weight=weights[indices])
        
        # Calculate predictions on the training set
        predictions = clf.predict(x)
        
        # Calculate error
        error = np.sum(weights * (predictions != y))
        
        # Calculate classifier weight
        classifier_weight = 0.5 * np.log((1 - error) / error)
        
        # Update sample weights
        weights *= np.exp(-classifier_weight * y * predictions)
        weights /= np.sum(weights)

def predict(classifiers, x_test) -> List[int]:
    """
    Make predictions using the trained boosting model.
    """
    predictions = np.zeros(len(x_test))
    
    for clf in classifiers:
        clf_prediction = clf.predict(x_test)
        predictions += clf_prediction
    
    # If the sum of classifiers is greater than 0, output 1, otherwise output -1
    return np.where(predictions > 0, 1, -1)

# Load breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize classifiers (you can use any classifiers supported by sklearn)
classifiers = [LogisticRegression() for _ in range(3)]

# Train the boosting model
fit(classifiers, X_train, y_train)

# Make predictions
predictions = predict(classifiers, X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
