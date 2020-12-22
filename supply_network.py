import numpy as np
from create_structure import *
from mat_algorithm import *



def main():
    Net_mat = create_matrix()
    Reach_mat = get_reach_matrix(Net_mat)
    #get_relation_division(Reach_mat)
    find_hierachy(Reach_mat)
    A = find_parts(Reach_mat)
    print(A)
    print(Net_mat)
    get_strong_subset_matrix(Net_mat)
    #find_all_reaches(Reach_mat, A)

    return

if __name__ == '__main__':
    main()