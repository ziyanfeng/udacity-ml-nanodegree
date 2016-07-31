#!/usr/bin/python

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


# def quicksort(array):
#     if len(array) <= 1:
#         return array
#     pivot = array[0]
#     less = []
#     equal = []
#     greater = []
#
#     for x in array:
#         if x < pivot:
#             less.append(x)
#         if x == pivot:
#             equal.append(x)
#         if x > pivot:
#             greater.append(x)
#     return quicksort(less) + equal + quicksort(greater)
#

# more concise version
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    return quicksort(less) + equal + quicksort(greater)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
