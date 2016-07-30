#!/usr/bin/python

"""Implement bubble sort in Python.
Input a list.
Output a sorted list."""


def bubblesort(array):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                unsorted = True
                array[i], array[i+1] = array[i+1], array[i]
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print bubblesort(test)
