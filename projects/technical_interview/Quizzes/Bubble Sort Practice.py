#!/usr/bin/python

"""Implement bubble sort in Python.
Input a list with no duplicates.
Output a sorted list."""


# # Method 1
# def bubblesort(array):
#     unsorted = True
#     while unsorted:
#         unsorted = False
#         for i in range(len(array) - 1):
#             if array[i] > array[i+1]:
#                 unsorted = True
#                 array[i], array[i+1] = array[i+1], array[i]
#     return array


# Method 2
def bubblesort(array):
    passnum = len(array) - 1
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(passnum):
            if array[i] > array[i+1]:
                unsorted = True
                array[i], array[i+1] = array[i+1], array[i]
        passnum -= 1
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print bubblesort(test)
