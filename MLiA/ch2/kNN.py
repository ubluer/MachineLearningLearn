#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# k Nearest Neighbors k邻近算法2阶

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
    # print('离样本距离', distances)
    sorted_dist_indices = argsort(array(distances))

    class_count = {}
    for i in range(knn):
        vote_label = labels[sorted_dist_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    sorted_class_count = sorted(class_count.items(),
                                key=lambda x: x[1], reverse=True)
    return sorted_class_count[0][0]


def file2matrix(filename):
    number_of_eigenvalues = 3
    fr = open(filename)
    array_of_lines = fr.readlines()
    number_of_lines = len(array_of_lines)
    return_mat = zeros((number_of_lines, number_of_eigenvalues))
    class_label_vector = []
    index = 0
    for line in array_of_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        return_mat[index, :] = list_from_line[0:number_of_eigenvalues]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1
    return return_mat, class_label_vector


def auto_norm(data_set):
    """
    归一化方法
    """
    min_values = data_set.min(0)
    max_values = data_set.max(0)
    ranges = max_values - min_values
    m = data_set.shape[0]
    norm_data_set = data_set - tile(min_values, (m, 1))
    norm_data_set = norm_data_set / tile(ranges, (m, 1))
    return norm_data_set, ranges, min_values


def dating_class_test():
    """
    约会网站数据测试
    """
    ho_radio = 0.1
    dating_data_mat, dating_labels = file2matrix('./data/datingTestSet2.txt')
    norm_mat, ranges, min_values = auto_norm(dating_data_mat)
    m = norm_mat.shape[0]
    num_test_vectors = int(m * ho_radio)
    error_count = 0.0
    for i in range(num_test_vectors):
        classifier_result = classify0(norm_mat[i, :], norm_mat[num_test_vectors:m, :],
                                      dating_labels[num_test_vectors:m], 10)
        print("the classifier came back with: %d, the ral answer is: %d" % (classifier_result, dating_labels[i]))
        if classifier_result != dating_labels[i]:
            error_count += 1.0
    print("this total rate is: %f" % (error_count / float(num_test_vectors)))
