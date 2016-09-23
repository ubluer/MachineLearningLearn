# -*- coding: utf-8 -*-
# 决策树算法,数据结构为 ,[特征1,特征2,..特征n,类别]

from math import log


def calc_shannon_ent(data_set):
    """
    计算一个集合的香农熵
    :param data_set: 矩阵数组，最后一列为分类信息
    :return: 香农熵
    """
    entries_size = len(data_set)
    labels = {}
    for feat_vec in data_set:
        current_label = feat_vec[-1]
        if current_label not in labels.keys():
            labels[current_label] = 0
        labels[current_label] += 1
    shannon_ent = 0.0
    for key in labels:
        prob = float(labels[key]) / entries_size
        shannon_ent += -prob * log(prob, 2)
    return shannon_ent


def create_data_set():
    data_set = [[1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'maybe'], [0, 0, 'no']]
    labels_set = ['xBox', 'PS4']
    return data_set, labels_set


def split_data_set(data_set, axis, value):
    ret_data_set = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis + 1:])
            ret_data_set.append(reduced_feat_vec)
    return ret_data_set


def choose_best_feature_to_split(data_set):
    feature_size = len(data_set[0]) - 1
    base_entropy = calc_shannon_ent(data_set)
    beat_info_gain = 0.0
    best_feature = -1
    for i in range(feature_size):
        # create unique classify 列表生成式
        feat_list = [example[i] for example in data_set]
        unique_val = set(feat_list)
        new_entropy = 0.0


data, labels = create_data_set()
print(calc_shannon_ent(data))
