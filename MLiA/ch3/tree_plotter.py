# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

decision_node = dict(boxstyle="sawtooth", fc="0.8")
leaf_node = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plot_node(node_txt, center_pt, parent_pt, node_type):
    create_plot.ax1.annotate(node_txt, xy=parent_pt, xycoords='axes fraction',
                             xytext=center_pt, textcoords='axes fraction',
                             va='center', ha='center',
                             bbox=node_type, arrowprops=arrow_args)


def create_plot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    create_plot.ax1 = plt.subplot(111, frameon=False)
    plot_node(U'decision', (0.5, 0.1), (0.1, 0.5), decision_node)
    plot_node(U'leaf', (0.8, 0.1), (0.3, 0.8), leaf_node)
    plt.show()


def get_leafs_size(tree):
    leafs_size = 0
    first_str = tree.keys()[0]
    second_dict = tree[first_str]
    for key in second_dict.keys():
        if isinstance(second_dict[key], dict):
            leafs_size += get_leafs_size(second_dict[key])
        else:
            leafs_size += 1
    return leafs_size


def get_tree_depth(tree):
    max_depth = 0
    first_str = tree.keys()[0]
    second_dict = tree[first_str]
    for key in second_dict.keys():
        if isinstance(second_dict[key], dict):
            this_depth = 1 + get_tree_depth(second_dict[key])
        else:
            this_depth = 1
        if this_depth > max_depth:
            max_depth = this_depth
    return max_depth


def retrieve_tree(i):
    list_of_trees = [{'xBox': {0: {'PS4': {0: 'no', 1: 'maybe'}}, 1: 'yes'}}]
    return list_of_trees[i]


create_plot()
