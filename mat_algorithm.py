import numpy as np
from basic_functions import *

def get_reach_matrix(matrix): #获得可达矩阵
    '''
    @description: 从邻接矩阵获得可达矩阵
    @matrix {list} list列表形式的矩阵，因此需要np.mat将其转化为矩阵
    @return: 01形式的可达矩阵
    @usage:
        matrix = [[0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        get_reach_matrix(matrix)
    '''
    A = matrix
    I = np.identity(len(A))
    newMat = A + I
    oldMat = newMat
    A_new = A
    flag = 0
    step = 1
    while flag == 0:
        oldMat = newMat
        A_new = Mat_reach(A, A_new)
        newMat = oldMat + (A_new + I)
        for i in range(len(newMat)):
            for j in range(len(newMat)):
                if newMat[i, j] >= 1:
                    newMat[i, j] = 1
        step += 1
        print(step)
        if (oldMat == newMat).all():
            flag = 1
            print(newMat)
            print('transfered to reach matrix')
            return newMat
def Mat_reach(A, A_new):
    for i in range(A.shape[0]):
        A[i][i] = 0
        A_new[i][i] = 0
    new_mat = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            for k in range(A.shape[0]):
                if A_new[i][k] == 1 and A[k][j] == 1:
                    new_mat[i][j] = 1
    return new_mat

def get_relation_division(matrix):
    '''
    @description: 关系划分
    @return: 打印出关系划分
    '''
    ones = []
    zeros = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j]:
                ones.append((i+1,j+1))
            else:
                zeros.append((i+1,j+1))
    print('ones', ones)
    print('zeros', zeros)

def find_before(matrix, j, list1):
    # list1 = []
    # for i in range(matrix.shape[0]):
    #     if matrix[i][j]:
    #         list1.append(i+1)
    # return list1
    reach_list = list1
    #before_list = []
    #both_list = []
    for i in range(matrix.shape[0]):
        if matrix[i][j]:
            if i+1 not in reach_list:
                #print(i)
                reach_list.append(i+1)
                A = find_before(matrix, i, reach_list)
                if A != []: #将之前的前因元素递归并入
                    for index in A:
                        if index not in reach_list:
                            reach_list.append(A)
    return reach_list

def get_reach_list(matrix, i):
    list1 = []
    for j in range(matrix.shape[0]):
        if matrix[i][j]:
            list1.append(j+1)
    return list1

def clr_pos(matrix, i):
    for m in range(matrix.shape[0]):
        matrix[m][i-1] = 0
    for n in range(matrix.shape[1]):
        matrix[i-1][n] = 0
    return matrix
def find_3_lists(Reach_mat):
    fronts = []
    reaches = []
    both_list = []
    phase_1 = []
    for i in range(Reach_mat.shape[1]):
        fronts.append(find_before(Reach_mat, i, []))
        reaches.append(get_reach_list(Reach_mat, i))
        both_list.append([])
        for j in fronts[i]:
            if j in reaches[i]:
                both_list[i].append(j)
        print(i + 1, reaches[i], '  ', fronts[i], '  ', both_list[i])
    for i in range(Reach_mat.shape[1]):
        if list_compare(reaches[i], both_list[i]) and len(reaches[i]) > 0:
            phase_1.append(i + 1)
    return phase_1
def find_parts(Reach_mat):
    fronts = []
    reaches = []
    both_list = []
    bases = []
    for i in range(Reach_mat.shape[1]):
        fronts.append(find_before(Reach_mat, i, []))
        reaches.append(get_reach_list(Reach_mat, i))
        both_list.append([])
        for j in fronts[i]:
            if j in reaches[i]:
                both_list[i].append(j)
        print(i + 1, reaches[i], '  ', fronts[i], '  ', both_list[i])
    for i in range(Reach_mat.shape[1]):
        if list_compare(both_list[i], fronts[i]):
            bases.append(i+1)
    return bases

def find_hierachy(Reach_mat):
    phase_1 = find_3_lists(Reach_mat)
    #phase_1 = [13, 19]
    print('phase1:', phase_1)
    mat_2 = Reach_mat
    for i in phase_1:
        mat_2 = clr_pos(mat_2, i)
    phase_2 = find_3_lists(mat_2)
    print('phase2:', phase_2)
    mat_3 = mat_2
    for i in phase_2:
        mat_3 = clr_pos(mat_3, i)
    phase_3 = find_3_lists(mat_3)
    print('phase3:', phase_3)
    mat_4 = mat_3
    for i in phase_3:
        mat_4 = clr_pos(mat_4, i)
    phase_4 = find_3_lists(mat_4)
    #phase_4 = [15, 16, 17]
    print('phase4:', phase_4)
    mat_5 = mat_4
    for i in phase_4:
        mat_5 = clr_pos(mat_5, i)
    phase_5 = find_3_lists(mat_5)
    print('phase5:', phase_5)
    mat_6 = mat_5
    for i in phase_5:
        mat_6 = clr_pos(mat_6, i)
    phase_6 = find_3_lists(mat_6)
    #phase_6 = [13, 19]
    print('phase6:', phase_6)
    return

def find_all_reaches(matrix, list1):
    list_n = []
    list_all = []
    list_common = []
    k = 0
    for i in list1:
        list_n.append(get_reach_list(matrix, i-1))
    for i in range(len(list_n)):
        for index in list_n[i]:
            if index not in list1 and index not in list_all:
                list_all.append(index)
    print(list_all)
    k=0
    for index in list_all:
        list_common.append([])
        for i in range(len(list_n)):
            if index in list_n[i]:
                list_common[k].append(list1[i])
        k += 1
    parts = []
    for i in range(len(list_common)):
        for index in list_common[i]:
            if index not in parts:
                parts.append(index)
    print('part 1', parts)
    return

def get_strong_subset_matrix(matrix): #获得强连接子集
    A = matrix
    A_new = A
    list_step = []
    list_pos = []
    for i in range(10):
        A_new = Mat_reach(A, A_new)
        for m in range(A.shape[0]):
            if A_new[m][m]:
                list_step.append(i+2)
                list_pos.append(m+1)

    print('step', list_step)
    print('pos', list_pos)
    return