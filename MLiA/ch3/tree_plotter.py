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


def plot_mid_text(center_pt, parent_pt, text):
    x_mid = (parent_pt[0] - center_pt[0]) / 2.0 + center_pt[0]
    y_mid = (parent_pt[1] - center_pt[1]) / 2.0 + center_pt[1]
    create_plot.ax1.text(x_mid, y_mid, text)


def plot_tree(tree, parent_pt, node_txt):
    leafs_size = get_leafs_size(tree)
    tree_depth = get_tree_depth(tree)
    first_str = list(tree.keys())[0]
    center_pt = (plot_tree.xoff + (1.0 + float(leafs_size)) / 2 / plot_tree.total_w,
                 plot_tree.yoff)
    plot_mid_text(center_pt, parent_pt, node_txt)
    plot_node(first_str, center_pt, parent_pt, decision_node)
    second_dict = tree[first_str]
    plot_tree.yoff -= 1.0 / plot_tree.total_d
    for key in second_dict.keys():
        if isinstance(second_dict[key],dict):
            plot_tree(second_dict[key], center_pt, str(key))
        else:
            plot_tree.xoff += 1.0 / plot_tree.total_w
            plot_node(second_dict[key], (plot_tree.xoff, plot_tree.yoff),
                      center_pt, leaf_node)
            plot_mid_text((plot_tree.xoff, plot_tree.yoff), center_pt,
                          str(key))
    plot_tree.yoff += 1.0 / plot_tree.total_d


def create_plot(in_tree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    create_plot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plot_tree.total_w = float(get_leafs_size(in_tree))
    plot_tree.total_d = float(get_tree_depth(in_tree))
    plot_tree.xoff = -0.5 / plot_tree.total_w
    plot_tree.yoff = 1.0
    plot_tree(in_tree, (0.5, 1.0), '')
    plt.show()


def get_leafs_size(tree):
    leafs_size = 0
    first_str = list(tree.keys())[0]
    second_dict = tree[first_str]
    for key in second_dict.keys():
        if isinstance(second_dict[key], dict):
            leafs_size += get_leafs_size(second_dict[key])
        else:
            leafs_size += 1
    return leafs_size


def get_tree_depth(tree):
    max_depth = 0
    first_str = list(tree.keys())[0]
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


create_plot(retrieve_tree(0))
