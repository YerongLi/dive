import numpy as np

class TreeNode():
    def __init__(self, data, feature_idx, feature_val, prediction_probs, information_gain) -> None:
        # Initialize the TreeNode with the following properties:
        # - data: The subset of data associated with this node.
        # - feature_idx: Index of the feature used for splitting at this node.
        # - feature_val: Value of the feature used for splitting at this node.
        # - prediction_probs: Probabilities of different classes for prediction at this node.
        # - information_gain: Information gain achieved by splitting at this node.
        self.data = data
        self.feature_idx = feature_idx
        self.feature_val = feature_val
        self.prediction_probs = prediction_probs
        self.information_gain = information_gain
        
        # Calculate the feature importance as the product of the number of samples at this node and the information gain.
        self.feature_importance = self.data.shape[0] * self.information_gain
        
        # Initialize the left and right children of this node as None.
        self.left = None
        self.right = None

    def node_def(self) -> str:
        # Define the description of the node based on whether it's a leaf or a splitting node.
        if (self.left or self.right):  # If the node has children (i.e., it's not a leaf node):
            # Return a string indicating that it's a splitting node, specifying the split condition.
            return f"NODE | Information Gain = {self.information_gain} | Split IF X[{self.feature_idx}] < {self.feature_val} THEN left O/W right"
        else:  # If the node has no children (i.e., it's a leaf node):
            # Calculate unique values and their counts in the labels of the subset of data at this leaf node.
            unique_values, value_counts = np.unique(self.data[:,-1], return_counts=True)
            # Create a string representation of label counts.
            output = ", ".join([f"{value}->{count}" for value, count in zip(unique_values, value_counts)])            
            # Return a string indicating that it's a leaf node, along with label counts and prediction probabilities.
            return f"LEAF | Label Counts = {output} | Pred Probs = {self.prediction_probs}"
