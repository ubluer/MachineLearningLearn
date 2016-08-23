import MLiA.ch2.kNN as kNN

test_group, test_labels = kNN.file2matrix('./data/datingTestSet2.txt')
# Matplotlib

# k值取训练样本的一半
# result = kNN.classify0([0, 0], test_group, test_labels, round(len(test_group) / 2))
# print('k个邻近的分类频数', result)

