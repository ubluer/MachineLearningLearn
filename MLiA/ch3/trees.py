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
    data_set = [[1, 1, 'yes'], [1, 0, 'yes'], [0, 1, 'maybe'], [0, 0, 'no']]
    labels_set = ['xBox', 'PS4']
    return data_set, labels_set


def split_data_set(data_set, axis, value):
    """
    将数据矩阵data在axis列使用提取值为value的子项
    """
    ret_data_set = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis + 1:])
            ret_data_set.append(reduced_feat_vec)
    return ret_data_set


def choose_best_feature_to_split(data_set):
    """
    计算每一列分割后的香农熵，取增加最多的
    """
    feature_size = len(data_set[0]) - 1
    base_entropy = calc_shannon_ent(data_set)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(feature_size):
        # create unique classify 列表生成式
        feat_list = [example[i] for example in data_set]
        unique_val = set(feat_list)
        new_entropy = 0.0
        for value in unique_val:
            sub_data_set = split_data_set(data_set, i, value)
            prob = len(sub_data_set) / float(len(data_set))
            new_entropy += prob * calc_shannon_ent(sub_data_set)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature


def majority_count(class_list):
    """
    投票选取class_list里最多的一项
    """
    class_count = {}
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote] = 0
        class_count[vote] += 1
    sorted_class_count = sorted(class_count.items, key=lambda x: x[1], reverse=True)
    return sorted_class_count[0][0]


def create_tree(data_set, labels):
    """
    递归计算决策树
    """
    class_list = [example[-1] for example in data_set]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(data_set[0]) == 1:
        return majority_count(class_list)
    best_feat = choose_best_feature_to_split(data_set)
    best_feat_label = labels[best_feat]
    my_tree = {best_feat_label: {}}
    del (labels[best_feat])
    feat_values = [example[best_feat] for example in data_set]
    unique_values = set(feat_values)
    for value in unique_values:
        sub_labels = labels[:]
        my_tree[best_feat_label][value] = create_tree(split_data_set(data_set,best_feat, value), sub_labels)
    return my_tree


data, labels = create_data_set()
print(choose_best_feature_to_split(data))
print(calc_shannon_ent(data))
print(create_tree(data,labels))
