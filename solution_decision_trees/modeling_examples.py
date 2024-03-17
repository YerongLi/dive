#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import sklearn
import sys
from sklearn import datasets, model_selection, metrics
import matplotlib.pyplot as plt

# Importing our from scratch models
from decision_tree import DecisionTree
from random_forest import RandomForestClassifier
from adaboost import AdaBoostClassifier


# # DecisionTree Examples

# ## Training on Iris Dataset

# In[12]:


iris = datasets.load_iris()

X = np.array(iris.data)
Y = np.array(iris.target)
iris_feature_names = iris.feature_names

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.25, random_state=0)
print("Train Shape:", X_train.shape)
print("Train Shape:", X_test.shape)


# In[6]:


# Building the tree
my_tree = DecisionTree(max_depth=4, min_samples_leaf=1, min_information_gain=0)
my_tree.train(X_train, Y_train)


# In[ ]:


# Let's see the tree
my_tree.print_tree()


# In[ ]:


# Let's see the Train performance
train_preds = my_tree.predict(X_set=X_train)
print("TRAIN PERFORMANCE")
print("Train size", len(Y_train))
print("True preds", sum(train_preds == Y_train))
print("Train Accuracy", sum(train_preds == Y_train) / len(Y_train))


# In[ ]:


# Let's see the Test performance
test_preds = my_tree.predict(X_set=X_test)
print("TEST PERFORMANCE")
print("Test size", len(Y_test))
print("True preds", sum(test_preds == Y_test))
print("Accuracy", sum(test_preds == Y_test) / len(Y_test))


# In[ ]:


# Feature importance
plt.bar(range(len(my_tree.feature_importances)), 
        list(my_tree.feature_importances.values()), tick_label=iris_feature_names)
plt.title("Feature Importance")
plt.xlabel("Feature")
plt.xticks(rotation=90)
plt.ylabel("Feature Importance")
# plt.show()


# ## Training on Breast Cancer Dataset

# In[ ]:


# Load data
data = datasets.load_breast_cancer()
X = data.data
Y = data.target
breast_cancer_feature_names = data.feature_names

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)
print("Train Shape:", X_train.shape)
print("Train Shape:", X_test.shape)


# In[ ]:


# Building the tree
my_tree_2 = DecisionTree(max_depth=4, min_samples_leaf=5, min_information_gain=0.05)
my_tree_2.train(X_train, Y_train)


# In[ ]:


my_tree_2.print_tree()


# In[ ]:


# Let's see the Train performance
train_preds = my_tree_2.predict(X_set=X_train)
print("TRAIN PERFORMANCE")
print("Train size", len(Y_train))
print("True preds", sum(train_preds == Y_train))
print("Train Accuracy", sum(train_preds == Y_train) / len(Y_train))


# In[ ]:


# Let's see the Test performance
test_preds = my_tree_2.predict(X_set=X_test)
print("TEST PERFORMANCE")
print("Test size", len(Y_test))
print("True preds", sum(test_preds == Y_test))
print("Accuracy", sum(test_preds == Y_test) / len(Y_test))


# In[ ]:


# Feature importance
plt.bar(range(len(my_tree_2.feature_importances)), 
        list(my_tree_2.feature_importances.values()), tick_label=breast_cancer_feature_names)
plt.xticks(rotation=90)
plt.title("Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Feature Importance")
# plt.show()

exit()
# ## Training on Diabetes Data (from OpenML)

# In[ ]:


diabetes = datasets.fetch_openml(name="diabetes", as_frame=False)


# In[ ]:


diabetes_features = np.array(diabetes.data)
print(diabetes_features.shape)
diabetes_labels = np.array([y=="tested_positive" for y in diabetes.target]).astype(int)
print(diabetes_labels.shape)


# In[ ]:


X_train, X_test, Y_train, Y_test = model_selection.train_test_split(diabetes_features, diabetes_labels, test_size=0.2, random_state=0)


# In[ ]:


# Lets see how model performs with different max_depth thresholds

train_accuracy_dict = {}
test_accuracy_dict = {}
# depth_occured = {}

for depth in range(2, 21):
    tree_model = DecisionTree(max_depth=depth, min_samples_leaf=1)
    tree_model.train(X_train, Y_train)

    # depth_occured[depth] = tree_model.current_de

    # Train performance
    train_preds = tree_model.predict(X_set=X_train)
    train_accuracy = sum(train_preds == Y_train) / len(Y_train)
    train_accuracy_dict[depth] = train_accuracy

    # Test performance
    test_preds = tree_model.predict(X_set=X_test)
    test_accuracy = sum(test_preds == Y_test) / len(Y_test)
    test_accuracy_dict[depth] = test_accuracy


# In[ ]:


plt.plot(train_accuracy_dict.keys(), train_accuracy_dict.values(), label="Train")
plt.plot(test_accuracy_dict.keys(), test_accuracy_dict.values(), label="Test")
plt.title("Accuracy vs Depth for Diabetes Dataset")
plt.xlabel("Max Depth Threshold")
plt.ylabel("Accuracy")
plt.legend()
plt.ylim(bottom=0.0)
plt.show()


# #### We can see that the tree starts to overfit after max_depth exceeds 5

# In[ ]:


opt_tree_model = DecisionTree(max_depth=5, min_samples_leaf=1)
opt_tree_model.train(X_train, Y_train)


# In[ ]:


train_preds = opt_tree_model.predict(X_set=X_train)
print("TRAIN PERFORMANCE")
print("Train size", len(Y_train))
print("True preds", sum(train_preds == Y_train))
print("Accuracy", sum(train_preds == Y_train) / len(Y_train))

test_preds = opt_tree_model.predict(X_set=X_test)
print("TEST PERFORMANCE")
print("Test size", len(Y_test))
print("True preds", sum(test_preds == Y_test))
print("Accuracy", sum(test_preds == Y_test) / len(Y_test))


# In[ ]:


opt_tree_model.print_tree()


# In[ ]:


# Feature importance
plt.bar(range(len(opt_tree_model.feature_importances)), 
        list(opt_tree_model.feature_importances.values()), tick_label=diabetes.feature_names)
plt.xticks(rotation=90)
plt.title("Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Feature Importance")
plt.show()


# # Random Forest Examples

# ## Training on Iris Dataset

# In[ ]:


iris = datasets.load_iris()

X = np.array(iris.data)
Y = np.array(iris.target)
iris_feature_names = iris.feature_names

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.25, random_state=0)
print("Train Shape:", X_train.shape)
print("Train Shape:", X_test.shape)


# In[ ]:


# Building random forest model
rf_model = RandomForestClassifier(n_base_learner=50, numb_of_features_splitting="sqrt")
rf_model.train(X_train, Y_train)


# In[ ]:


# Performans increases when compared to the basic DecisionTree
train_preds = rf_model.predict(X_set=X_train)
print("TRAIN PERFORMANCE")
print("Train size", len(Y_train))
print("True preds", sum(train_preds == Y_train))
print("Accuracy", sum(train_preds == Y_train) / len(Y_train))

test_preds = rf_model.predict(X_set=X_test)
print("TEST PERFORMANCE")
print("Test size", len(Y_test))
print("True preds", sum(test_preds == Y_test))
print("Accuracy", sum(test_preds == Y_test) / len(Y_test))


# ## Training on Breast Cancer Dataset

# In[ ]:


# Load data
data = datasets.load_breast_cancer()
X = data.data
Y = data.target
breast_cancer_feature_names = data.feature_names

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)
print("Train Shape:", X_train.shape)
print("Train Shape:", X_test.shape)


# In[ ]:


# Building random forest model
rf_model_2 = RandomForestClassifier(n_base_learner=100, 
                                    max_depth=4, min_samples_leaf=5, min_information_gain=0.05)
rf_model_2.train(X_train, Y_train)


# In[ ]:


# Performans increases when compared to the basic DecisionTree
train_preds = rf_model_2.predict(X_set=X_train)
print("TRAIN PERFORMANCE")
print("Train size", len(Y_train))
print("True preds", sum(train_preds == Y_train))
print("Accuracy", sum(train_preds == Y_train) / len(Y_train))

test_preds = rf_model_2.predict(X_set=X_test)
print("TEST PERFORMANCE")
print("Test size", len(Y_test))
print("True preds", sum(test_preds == Y_test))
print("Accuracy", sum(test_preds == Y_test) / len(Y_test))


# ## Training on Diabetes Data (from OpenML)

# In[ ]:


diabetes = datasets.fetch_openml(name="diabetes", as_frame=False)


# In[ ]:


diabetes_features = np.array(diabetes.data)
print(diabetes_features.shape)
diabetes_labels = np.array([y=="tested_positive" for y in diabetes.target]).astype(int)
print(diabetes_labels.shape)

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(diabetes_features, diabetes_labels, test_size=0.2, random_state=0)


# In[ ]:


rf_model_3 = RandomForestClassifier(n_base_learner=200, numb_of_features_splitting=None,
                                     max_depth=5, min_samples_leaf=1)
rf_model_3.train(X_train, Y_train)


# In[ ]:


# Performance increases when compared to basic decision tree
train_preds = rf_model_3.predict(X_set=X_train)
print("TRAIN PERFORMANCE")
print("Train size", len(Y_train))
print("True preds", sum(train_preds == Y_train))
print("Accuracy", sum(train_preds == Y_train) / len(Y_train))

test_preds = rf_model_3.predict(X_set=X_test)
print("TEST PERFORMANCE")
print("Test size", len(Y_test))
print("True preds", sum(test_preds == Y_test))
print("Accuracy", sum(test_preds == Y_test) / len(Y_test))


# In[ ]:


# Feature importance of RandomForest Model
plt.bar(range(len(rf_model_3.feature_importances)), 
        list(rf_model_3.feature_importances), tick_label=diabetes.feature_names)
plt.xticks(rotation=90)
plt.title("Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Feature Importance")
plt.show()


# # AdaBoost Examples

# ## Training on Iris Dataset

# In[ ]:


iris = datasets.load_iris()

X = np.array(iris.data)
Y = np.array(iris.target)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

model = AdaBoostClassifier(n_base_learner=50)
model.train(X_train, y_train)

train_accuracy = sum(model.predict(X=X_train) == y_train) / len(y_train)
test_accuracy = sum(model.predict(X=X_test) == y_test) / len(y_test)
print("Our Model Performance")
print("Train Accuracy: ", train_accuracy)
print("Test Accuracy: ", test_accuracy)


# In[ ]:


iris = datasets.load_iris()

X = np.array(iris.data)
Y = np.array(iris.target)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

model = sklearn.ensemble.AdaBoostClassifier(n_estimators=50)
model.fit(X_train, y_train)

train_accuracy = sum(model.predict(X=X_train) == y_train) / len(y_train)
test_accuracy = sum(model.predict(X=X_test) == y_test) / len(y_test)
print("Sklearn Model Performance")
print("Train Accuracy: ", train_accuracy)
print("Test Accuracy: ", test_accuracy)


# ## Training on Breast Cancer Dataset

# In[ ]:


data = datasets.load_breast_cancer()

X = np.array(data.data)
Y = np.array(data.target)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

model = AdaBoostClassifier(n_base_learner=50)
model.train(X_train, y_train)

train_accuracy = sum(model.predict(X=X_train) == y_train) / len(y_train)
test_accuracy = sum(model.predict(X=X_test) == y_test) / len(y_test)
print("Our Model Performance")
print("Train Accuracy: ", train_accuracy)
print("Test Accuracy: ", test_accuracy)


# In[ ]:


data = datasets.load_breast_cancer()

X = np.array(data.data)
Y = np.array(data.target)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

model = sklearn.ensemble.AdaBoostClassifier(n_estimators=50)
model.fit(X_train, y_train)

train_accuracy = sum(model.predict(X=X_train) == y_train) / len(y_train)
test_accuracy = sum(model.predict(X=X_test) == y_test) / len(y_test)
print("Sklearn Model Performance")
print("Train Accuracy: ", train_accuracy)
print("Test Accuracy: ", test_accuracy)


# ## Training on Diabetes Data (from OpenML)

# In[ ]:


diabetes = datasets.fetch_openml(name="diabetes", as_frame=False)
diabetes_features = np.array(diabetes.data)
print(diabetes_features.shape)
diabetes_labels = np.array([y=="tested_positive" for y in diabetes.target]).astype(int)
print(diabetes_labels.shape)

X_train, X_test, y_train, y_test = model_selection.train_test_split(diabetes_features, diabetes_labels, test_size=0.2, random_state=0)


# In[ ]:


model = AdaBoostClassifier(n_base_learner=50)
model.train(X_train, y_train)

train_accuracy = sum(model.predict(X=X_train) == y_train) / len(y_train)
test_accuracy = sum(model.predict(X=X_test) == y_test) / len(y_test)
print("Our Model Performance")
print("Train Accuracy: ", train_accuracy)
print("Test Accuracy: ", test_accuracy)


# In[ ]:


model = sklearn.ensemble.AdaBoostClassifier(n_estimators=50)
model.fit(X_train, y_train)

train_accuracy = sum(model.predict(X=X_train) == y_train) / len(y_train)
test_accuracy = sum(model.predict(X=X_test) == y_test) / len(y_test)
print("Sklearn Model Performance")
print("Train Accuracy: ", train_accuracy)
print("Test Accuracy: ", test_accuracy)


# ## Some Simulations for Understanding the # of Base Learners in AdaBoost

# In[ ]:


data = datasets.load_breast_cancer()

X = np.array(data.data)
Y = np.array(data.target)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

# model = AdaBoostClassifier(n_base_learner=10)
# model.train(X_train, y_train)

train_accuracy_list = []
test_accuracy_list = []
for n_base_learner in range(1, 150, 3):
    model = AdaBoostClassifier(n_base_learner)
    model.train(X_train, y_train)
    train_accuracy_list.append(sum(model.predict(X=X_train) == y_train) / len(y_train))
    test_accuracy_list.append(sum(model.predict(X=X_test) == y_test) / len(y_test))

plt.plot(list(range(1, 150, 3)), train_accuracy_list, color='red', label='train')
plt.plot(list(range(1, 150, 3)), test_accuracy_list, color='green', label='test')
plt.title("Our AdaBoostClassifier Performance")
plt.xlabel('# of Base Learner')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


# In[ ]:


train_accuracy_list = []
test_accuracy_list = []
n_estimaters_list = []
for n_base_learner in range(1, 150, 3):
    model = sklearn.ensemble.AdaBoostClassifier(n_estimators=n_base_learner, learning_rate=0.2, random_state=0)
    model.fit(X_train, y_train)
    train_accuracy_list.append(sum(model.predict(X_train) == y_train) / len(y_train))
    test_accuracy_list.append(sum(model.predict(X_test) == y_test) / len(y_test))
    n_estimaters_list.append(len(model.estimators_))

plt.plot(list(range(1, 150, 3)), train_accuracy_list, color='red', label='train')
plt.plot(list(range(1, 150, 3)), test_accuracy_list, color='green', label='test')
plt.title("Sklearn AdaBoostClassifier Performance")
plt.xlabel('# of Base Learner')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

