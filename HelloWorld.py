# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import tree

smooth = 0
bumpy = 1

color = {}
color['red'] = 0
color['orange'] = 1
color['green'] = 2
color['blue'] = 3
color['yellow'] = 4
color['purple'] = 5

apple = 0
orange = 1

features = [[140, smooth, color['red']], [130, smooth, color['red']], [150, bumpy, color['orange']], [170, bumpy, color['orange']]]
labels = [apple, apple, orange, orange]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
clf = clf.predict([[200, bumpy, color['orange']]])
print(clf)