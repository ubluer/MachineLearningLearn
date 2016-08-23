#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kNN k邻近算法2阶

from numpy import *


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, data_set, labels, knn):
    data_set_size = data_set.shape[0]
    print('训练样本大小:', data_set_size)
    # 将输入扩充成 (样本大小*1)的矩阵,并计算该矩阵的元素与训练样本的差;
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    print('离样本距离', distances)
    # noinspection PyTypeChecker
    sorted_dist_indices = argsort(distances)

    class_count = {}
    for i in range(knn):
        vote_label = labels[sorted_dist_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    sorted_class_count = sorted(class_count.items(),
                                key=lambda x: x[1], reverse=True)
    return sorted_class_count


test_group, test_labels = create_data_set()
# k值取训练样本的一半
result = classify0([0, 0], test_group, test_labels, round(len(test_group) / 2))
print('k个邻近的分类频数', result)
