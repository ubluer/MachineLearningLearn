# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from os import listdir

from numpy import *

from MLiA.ch2.kNN import classify0


def img2vector(filename):
    return_value = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        line_str = fr.readline()
        for j in range(32):
            return_value[0, 32 * i + j] = int(line_str[j])
    return return_value


def handwriting_class_test():
    top_folder = './data/digits'
    training_folder = '%s/trainingDigits' % top_folder
    test_folder = '%s/testDigits' % top_folder

    hw_labels = []
    training_file_list = listdir(training_folder)
    m = len(training_file_list)
    training_mat = zeros((m, 1024))
    for i in range(m):
        # 解析文件名
        file_name_str = training_file_list[i]
        file_str = file_name_str.split('.')[0]
        class_num_str = int(file_name_str.split('_')[0])
        hw_labels.append(class_num_str)
        training_mat[i:] = img2vector('%s/%s' % (training_folder, file_name_str))
    test_file_list = listdir(test_folder)
    error_count = 0.0
    m_test = len(test_file_list)
    for i in range(m_test):
        file_name_str = test_file_list[i]
        file_str = file_name_str.split('.')[0]
        class_num_str = int(file_name_str.split('_')[0])
        vector_under_test = img2vector('%s/%s' % (test_folder, file_name_str))
        classifier_result = classify0(vector_under_test, training_mat, hw_labels, 3)

        if class_num_str != classifier_result:
            error_count += 1.0
            print('file:%s, classifier: %d, real: %d' % (file_str, classifier_result, class_num_str))
    print('the number of errors: %d' % error_count)
    print('error rate: %f' % (error_count / float(m_test)))


handwriting_class_test()
