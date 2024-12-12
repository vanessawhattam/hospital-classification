# Assignment
# You are now ready to begin assessing your data and build initial models. 
# Randall Cunningham would like you to build decision trees. Your new assignment requires you to build classification trees and regression trees. 
# Use the data file calihospital.txt for this assignment.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#from sklearn.feature_extraction.image import grid_to_graph
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split

#For displaying the tree
import graphviz
from six import StringIO
from IPython.display import Image, display
import pydotplus

hosp_data = pd.read_table('data/calihospital.txt')
hosp_data.dtypes

# Decide on the predictor variables you use for these analyses.

# Using operating income as a target variable, create a tree (1 pt.)
#regression tree
hosp_one = hosp_data[['InOperExp', 'OperRev', 'AvlBeds', 'NoFTE']]

# Get the column names for the plot later
col_names = list(hosp_one.columns.values)

# Fit the tree, limiting the leaves so it's a manageable size
tree1 = tree.DecisionTreeRegressor(min_samples_split=3,min_samples_leaf=3).fit(hosp_one,hosp_data.OperInc)

# Plot and show the tree
plt.figure(figsize=(30, 24))
tree.plot_tree(tree1, feature_names=col_names,filled=True,rounded=True, fontsize=10)
plt.show()


# Using operating revenue as a target variable, create a tree (1 pt.)
#regressiontree
hosp_two = hosp_data[['OutOperExp', 'OperInc', 'AvlBeds', 'NetPatRev']]

# Get the column names for the plot later
col_names = list(hosp_two.columns.values)

# Fit the tree, limiting the leaves so it's a manageable size
tree2 = tree.DecisionTreeRegressor(min_samples_split=4,min_samples_leaf=4).fit(hosp_two,hosp_data.OperRev)


plt.figure(figsize=(30, 24))  # Increase the figure size
tree.plot_tree(tree2, feature_names=col_names, filled=True, rounded=True, fontsize=10)  # Decrease fontsize
plt.show()


# Using TypeControl as a target variable, create a tree (1 pt.)
#classification tree
hosp_three = hosp_data[['NoFTE', 'Teaching', 'AvlBeds', 'NetPatRev']]

# One-hot encode categorical variables
hosp_three.loc[:, 'Teaching'] = pd.get_dummies(hosp_three['Teaching'], drop_first=True)
classnames = list(hosp_data.TypeControl.unique())

# Extract features and target variable
features = hosp_three
target = hosp_data['TypeControl']

# Fit the decision tree classifier
tree3 = tree.DecisionTreeClassifier().fit(features, target)

# Plot the decision tree
plt.figure(figsize=(30, 24))
tree.plot_tree(tree3, feature_names=features.columns, class_names=classnames, filled=True, rounded=True, fontsize=10)
plt.show()

predicted = tree3.predict(hosp_three)
print(metrics.classification_report(hosp_data.TypeControl, predicted))

cm = metrics.confusion_matrix(hosp_data.TypeControl, predicted)
print(cm)

# Using DonorType as a target variable, create a tree (1 pt.)
#classification tree
hosp_four = hosp_data[['TypeControl', 'OperInc', 'OperRev', 'NetPatRev']]

# One-hot encode categorical variables and drop the original columns
hosp_four.loc[:, 'TypeControl'] = pd.get_dummies(hosp_four['TypeControl'], drop_first=True)
#hosp_four = pd.get_dummies(hosp_four, columns=['Teaching', 'TypeControl'], drop_first=True)

classnames = list(hosp_data.DonorType.unique())

# Extract features and target variable
features4 = hosp_four
target = hosp_data['DonorType']

# Fit the decision tree classifier
tree4 = tree.DecisionTreeClassifier().fit(features4, target)

# Plot the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(tree4, feature_names=features4.columns, class_names=classnames, filled=True, rounded=True, fontsize=10)
plt.show()

predicted = tree4.predict(hosp_four)
print(metrics.classification_report(hosp_data.DonorType, predicted))

cm = metrics.confusion_matrix(hosp_data.DonorType, predicted)
print(cm)

