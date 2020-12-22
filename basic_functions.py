import numpy as np

def list_compare(list1, list2):
    #to determine whether two lists are the same
    A = len(list1)
    B = len(list2)
    if A != B:
        return False
    for i in range(A):
        if list1[i] != list2[i]:
            return False
    return True
