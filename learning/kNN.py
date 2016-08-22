#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, data_set, labels, knn):
    data_set_size = data_set.shape[0]
    print '训练样本大小:', data_set_size
    # 将输入扩充成 (样本大小*1)的矩阵,并计算该矩阵的元素与训练样本的差;
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)

    print diff_mat
    for i in range(knn):
        print (i)


test_group, test_labels = create_data_set()
classify0([0, 0], test_group, test_labels, 3)
