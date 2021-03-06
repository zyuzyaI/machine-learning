# -*- coding: utf-8 -*-
"""knn_and _gridsearch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OygTL5_ooh4D7uU2worMvfeRaf2_ceuh
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

X, X_test, y, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X.shape, y.shape, X_test.shape, y_test.shape)

def grid_seach_knn(X, y, k_neighbors=10, X_test=None, y_test=None):
    # X - numpy array (matrix)
    # y - numpy array (vector)
    clf_knn = KNeighborsClassifier()
    param_grid = {
    'n_neighbors': np.arange(2, k_neighbors), # can be, [1, 2, 3, 4]
    'weights': ['uniform', "distance"],
    'metric': ['manhattan', 'euclidean']
    }

    search = GridSearchCV(clf_knn, param_grid, n_jobs=-1, cv=5, refit=True, scoring='accuracy')
    search.fit(X, y)

    print(search.best_params_)
    if (X_test is not None) and (y_test is not None):
        print(accuracy_score(y_test, search.best_estimator_.predict(X_test)))
    else:
        print(accuracy_score(y, search.best_estimator_.predict(X)))
    return search.best_estimator_

grid_seach_knn(X, y, X_test=X_test, y_test=y_test)

