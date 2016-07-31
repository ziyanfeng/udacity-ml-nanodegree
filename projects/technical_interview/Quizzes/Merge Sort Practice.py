#!/usr/bin/python

"""Implement merge sort in Python.
Input a list.
Output a sorted list."""


def mergesort(array):
    if len(array) <= 1:
        return array
    else:
        result, mid = [], len(array) // 2
        lefthalf = mergesort(array[:mid])
        righthalf = mergesort(array[mid:])
        # merge
        while len(lefthalf) > 0 and len(righthalf) > 0:
            if lefthalf[0] < righthalf[0]:
                result.append(lefthalf[0])
                lefthalf.pop(0)
            else:
                result.append(righthalf[0])
                righthalf.pop(0)
        result += lefthalf
        result += righthalf
        return result


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14, 3]
print mergesort(test)
