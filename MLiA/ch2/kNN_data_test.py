# -*- coding: utf-8 -*-
from MLiA.ch2 import kNN

test_group, test_labels = kNN.file2matrix('./data/datingTestSet2.txt')
# Matplotlib 展示数据选择特征值

# fig = pyplot.figure()
# ax = fig.add_subplot(111)
# ax.scatter(test_group[:, 1], test_group[:, 0], 15*array(test_labels), 15*array(test_labels))
# pyplot.show()

# 归一化数据
norm_mat,ranges,min_values = kNN.auto_norm(test_group)
# k值取训练样本的一半
# result = kNN.classify0([0, 0], test_group, test_labels, round(len(test_group) / 2))
# print('k个邻近的分类频数', result)

kNN.dating_class_test()
