# -*- coding: utf-8 -*-
from matplotlib import pyplot
from numpy import *

from MLiA.ch2 import kNN

test_group, test_labels = kNN.file2matrix('./data/datingTestSet2.txt')
# Matplotlib

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.scatter(test_group[:, 1], test_group[:, 0], 15 * array(test_labels), 15 * array(test_labels))
pyplot.show()
