#!/usr/bin/python

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    if len(input_array) == 0:
        return -1
    left = 0
    right = len(input_array) - 1
    mid = int((right + left) / 2)
    while right > left and input_array[mid] != value:
        if input_array[mid] < value:
            left = mid + 1
            mid = int((right + left) / 2)
        else:
            right = mid - 1
            mid = int((right + left) / 2)
    if input_array[mid] == value:
        return mid
    else:
        return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
test_val3 = 1
test_val4 = 29
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, test_val3)
print binary_search(test_list, test_val4)
print binary_search(test_list, 0)
print binary_search(test_list, 100)

print binary_search([1], 1)
print binary_search([1], 0)
print binary_search([1], 2)

print binary_search([], 0)

