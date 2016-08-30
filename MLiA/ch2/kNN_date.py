from MLiA.ch2.kNN import *


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


def classify_person():
    result_list = ['not at all', 'in small doses', 'in large doses']
    percent_tats = float(input('percentage of time spent playing video game?'))
    ff_miles = float(input('frequent flier miles earned per year?'))
    ice_cream = float(input("liters of ice cream consumed per year?"))
    dating_data_mat, dating_labels = file2matrix('./data/datingTestSet2.txt')
    norm_mat, ranges, min_values = auto_norm(dating_data_mat)
    in_arr = array([ff_miles, percent_tats, ice_cream])
    classifier_result = classify0((in_arr - min_values) / ranges, norm_mat, dating_labels, 10)
    print('You will probably like this person ', result_list[classifier_result - 1])
    return classifier_result
