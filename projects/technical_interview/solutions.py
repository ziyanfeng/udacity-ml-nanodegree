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


# def question2(a):
#     palins = []
#     if len(a) <= 1:
#         palins.append(a)
#     elif a == a[::-1]:
#         palins.append(a)
#     else:
#         while len(a) > 1:
#             for i in range(len(a) + 1):
#                 if a[:i] == a[:i][::-1]:
#                     palins.append(a[:i])
#             a = a[1:]
#     l = [(len(p), i) for i, p in enumerate(palins)]
#     longest_i = max(l)[1]
#     return palins[longest_i]


def is_palin_helper(a, table, start, finish):
    if start < 0 or finish >= len(a):
        return False
    if start > finish:
        return False
    if table[start][finish] is None:
        is_palin = is_palin_helper(a, table, start+1, finish-1) and a[start] == a[finish]
        table[start][finish] = is_palin
        return is_palin
    else:
        return table[start][finish]


def question2(a):
    if len(a) <= 1:
        return a
    is_palin = [[None] * len(a) for i in range(len(a))]
    # all substrings of length 1 are palindromes
    for i in range(len(a)):
        is_palin[i][i] = True

    # check if substring of length 2 is palindrome
    for i in range(len(a) - 1):
        if a[i] == a[i+1]:
            is_palin[i][i+1] = True

    # check substrings of length greater than 2
    for i in range(len(a)):
        for j in range(len(a)):
            is_palin_helper(a, is_palin, i, j)

    # find the longest panlindromic substring
    length = 0
    longest = ''
    for i in range(len(a)):
        for j in range(len(a)):
            if is_palin[i][j]:
                if j - i + 1 > length:
                    length = j - i + 1
                    longest = a[i:j+1]
    return longest


# Test Cases
# Should print 'a'
print question2('abc')
# Should print 'a'
print question2('a')
# Should print ''
print question2('')
# Should print 'aba'
print question2('aba')
# Should print 'abcba'
print question2('abcba')
# Should print 'geeksskeeg'
print question2("forgeeksskeegfor")
# Should print 'hpyyph'
print question2("anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeo"
                "uvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqd"
                "nwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmo"
                "mnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzu"
                "lhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrv"
                "abthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcy"
                "sfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzi"
                "fwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyju"
                "sppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruu"
                "wvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucw"
                "usjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacci"
                "flcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjm"
                "hmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcoc"
                "soiqtfuoazxdayricnmwcg")
# Should print 'gykrkyg'
print question2("zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhciha"
                "cqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhd"
                "mbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpth"
                "rmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnn"
                "wzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarj"
                "jdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgs"
                "fbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlw"
                "kmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqe"
                "ftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanv"
                "jpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgm"
                "ehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhc"
                "sofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgyk"
                "rkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqx"
                "oqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxrel"
                "dbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrekts"
                "nfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir")

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
    if len(G) < 1:
        return G
    nodes = set(G.keys())
    mst = {}
    start = G.keys()[0]
    mst[start] = []

    while len(mst.keys()) < len(nodes):
        min_w = float('inf')
        min_edge = None
        for node in mst.keys():
            edges = [(weight, vertex) for (vertex, weight) in G[node] if vertex not in mst.keys()]
            if len(edges) > 0:
                w, v = min(edges)
                if w < min_w:
                    min_w = w
                    min_edge = (node, v)
        mst[min_edge[0]].append((min_edge[1], min_w))
        mst[min_edge[1]] = [(min_edge[0], min_w)]
    return mst


# Test Cases
# Should print {}
print question3({})
# Should print {'A': []}
print question3({'A': []})
# Should print
# {'A': [('E', 1)],
#  'C': [('D', 3)],
#  'B': [('E', 2), ('D', 2)],
#  'E': [('A', 1), ('B', 2)],
#  'D': [('B', 2), ('C', 3)]}
print question3({'A': [('B', 3), ('E', 1)], 'B': [('A', 3), ('C', 9), ('D', 2), ('E', 2)],
                 'C': [('B', 9), ('D', 3), ('E', 7)], 'D': [('B', 2), ('C', 3)],
                 'E': [('A', 1), ('B', 2), ('C', 7)]})
# Should print
# {'A': [('D', 5), ('B', 7)],
#  'C': [('E', 5)],
#  'B': [('A', 7), ('E', 7)],
#  'E': [('B', 7), ('C', 5), ('G', 9)],
#  'D': [('A', 5), ('F', 6)],
#  'G': [('E', 9)],
#  'F': [('D', 6)]}
print question3({'A': [('B', 7), ('D', 5)], 'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
                 'C': [('B', 8), ('E', 5)], 'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
                 'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
                 'F': [('D', 6), ('E', 8),  ('G', 11)], 'G': [('E', 9), ('F', 11)]})

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




