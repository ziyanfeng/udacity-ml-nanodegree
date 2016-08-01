#!/usr/bin/python

# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a boolean True or False.


def get_anagrams(t):
    if len(t) <= 1:
        return [t]
    else:
        anagrams = []
        for i, letter in enumerate(t):
            anagrams += [letter + parts for parts in get_anagrams(t[:i] + t[i + 1:])]
        return anagrams


def question1(s, t):
    if s == '' or t == '':
        return False
    elif s == t:
        return True
    else:
        anagrams = get_anagrams(t)
        for anagram in anagrams:
            if anagram in s:
                return True
        return False


# Test Cases
# Should print False
print question1('', '')
# Should print False
print question1('', 'a')
# Should print False
print question1('a', '')
# Should print True
print question1('udacity', 'udacity')
# Should print True
print question1('udacity', 'ad')


# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.






# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)


def question3(G):













# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
# For example, the root is a common ancestor of all nodes on the tree, but if both nodes are
# descendents of the root's left child, then that left child might be the lowest common ancestor.
# You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
# The function definition should look like question4(T, r, n1, n2), where T is the tree represented
# as a matrix, where the index of the list is equal to the integer stored in that node and a 1
# represents a child node, r is a non-negative integer representing the root, and n1 and n2 are
# non-negative integers representing the two nodes in no particular order. For example, one test case might be
#
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.
















# Question 5
# Find the element in a singly linked list that's m elements from the end. For example, if a
# linked list has 5 elements, the 3rd element from the end is the 3rd element. The function
# definition should look like question5(ll, m), where ll is the first node of a linked list
# and m is the "mth number from the end". You should copy/paste the Node class below to use
# as a representation of a node in the linked list. Return the value of the node at that position.
#
# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None


