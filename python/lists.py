#!/usr/bin/env python

import itertools

# Worth noting, since the list object is mutable all solutions here
# attempt to return a new list, to preserve data integrity.
# This is especially apparent in the reverse list question, where
# using the list.reverse builtin will cause the li list to be mutated.

li = list(range(10))
liS = ['hi']
liN = []

# 1.01 - Last Element in a List
def last(l):
    if not l:
        return None
    return l[-1]

assert(last(li) == 9)
assert(last(liS) == 'hi')
assert(last(liN) == None)
print("1.01 -- PASSED")

# 1.02 Last but one
def second_last(l):
    if len(l) < 2:
        return None
    return l[-2]

assert(second_last(li) == 8)
assert(second_last(liS) == None)
assert(second_last(liN) == None)
print("1.02 -- PASSED")

# 1.03 Kth Element
def kth_element(l, k):
    if abs(k) > len(l):
        return None
    return l[k]

assert(kth_element(li, 3) == 3)
assert(kth_element(li, -3) == 7)
assert(kth_element(liN, 4) == None)
assert(kth_element(liN, -4) == None)
print("1.03 -- PASSED")

# 1.04 Size of List
def list_size(l):
    return len(l)

assert(list_size(li) == 10)
assert(list_size(liS) == 1)
assert(list_size(liN) == 0)
print("1.04 -- PASSED")

# 1.05 Reverse List
def list_reverse(l):
    """ We could use l.reverse() here, but that mutates the list. """
    return l[::-1]

assert(list_reverse(li) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
assert(list_reverse(liS) == ['hi'])
assert(list_reverse(liN) == [])
print("1.05 -- PASSED")

# 1.06 Palindrome
def is_palindrome(l):
    return l == list_reverse(l)

assert(is_palindrome(li) == False)
assert(is_palindrome(liS) == True)
assert(is_palindrome(liN) == True)
assert(is_palindrome([1,2,1]) == True)
print("1.06 -- PASSED")

# 1.07 Flatten
def flatten(l):
    res = []
    for item in l:
        if isinstance(item, list):
            res.extend(flatten(item))
        else:
            res.append(item)
    return res

assert(flatten(li) == li)
assert(flatten(liN) == liN)
assert(flatten(liS) == liS)
assert(flatten([1, [2, 3], 4]) == [1, 2, 3, 4])
assert(flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6])
print("1.07 -- PASSED")

# 1.08 Eliminate Consecuative Duplicates
def compress(l):
    if len(l) < 2:
        return l
    prev = l[0]
    res = [prev]
    for i in l[1:]:
        if not i == prev:
            res.append(i)
        prev = i
    return res

assert(compress([1,2,2,3,2,4,4,4,4]) == [1,2,3,2,4])
assert(compress([1,1,1,1,1]) == [1])
assert(compress(liS) == ['hi'])
assert(compress(liN) == [])
print("1.08 -- PASSED")

# 1.09 Pack Duplicates to Sublist TODO
def pack(l):
    if not l:
        return []

#assert(pack([1,2,2,3,2,4,4,4,4]) == [[1],[2, 2],[3],[2],[4,4,4,4]])
#assert(pack([1,1,1,1,1]) == [[1,1,1,1,1]])
#assert(pack(liN) == [])
#print("1.09 -- PASSED")

# 1.10 Run-length TODO

# 1.11 TODO

# 1.12 TODO

# 1.13 #TODO

# 1.14 Duplicate Items
def dupli(l):
    return flatten([[item]*2 for item in l])

assert(dupli(li) == [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9])
assert(dupli(liN) == [])
print("1.14 -- PASSED")

# 1.15
def n_dupli(l, n):
    return flatten([[item]*n for item in l])

assert(n_dupli(li, 2) == [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9])
assert(n_dupli([1,2], 3) == [1,1,1,2,2,2])
assert(n_dupli(liN, 5) == [])
print("1.15 -- PASSED")

# 1.16 Drop Nth element
def drop(l, n):
    return [item for i, item in enumerate(l, start=1) if not i%n == 0]

assert(drop(li, 2) == [0, 2, 4, 6, 8])
assert(drop(li, 9) == [0, 1, 2, 3, 4, 5, 6, 7, 9])
assert(drop(liN, 3) == [])
print("1.16 -- PASSED")


#1.17 Split List
def split(l, n):
    return l[0:n], l[n:]

assert(split(li, 2) == ([0,1], [2,3,4,5,6,7,8,9]))
assert(split(liN, 3) == ([], []))
print("1.17 -- PASSED")

#1.18 Slice
def slice(l, i, k):
    return l[i:k+1]

assert(slice(li, 0, 2) == [0, 1, 2])
assert(slice(li, 1, 3) == [1, 2, 3])
assert(slice(liN, 2, 4) == [])
print("1.18 -- PASSED")

# 1.19 Rotate
def rotate(l, n):
    return l[n:]+l[0:n]

assert(rotate(li, 0) == [0,1,2,3,4,5,6,7,8,9])
assert(rotate(li, 1) == [1,2,3,4,5,6,7,8,9,0])
assert(rotate(li, 3) == [3,4,5,6,7,8,9,0,1,2])
assert(rotate(liN, 5) == [])
print("1.19 -- PASSED")

# 1.20 Remove Kth
def remove_at(l, n):
    return l[:n]+l[n+1:]

assert(remove_at(li, 0) == [1,2,3,4,5,6,7,8,9])
assert(remove_at(li, 1) == [0,2,3,4,5,6,7,8,9])
assert(remove_at(li, 9) == [0,1,2,3,4,5,6,7,8])
assert(remove_at(liN, 5) == [])
print("1.20 -- PASSED")

# 1.21 Insert in list
def insert_at(l, n, a):
    return l[:n]+[a]+l[n:]

assert(insert_at(li, 0, 2) == [2,0,1,2,3,4,5,6,7,8,9])
assert(insert_at(liN, 4, 1) == [1]) # Not sure if ideal behaviour
print("1.21 -- PASSED")

# 1.22 Range
def new_range(lower, upper):
    return list(range(lower, upper+1))

assert(new_range(0, 2) == [0, 1, 2])
print("1.22 -- PASSED")

# 1.23-1.25 SKIP: Can't test, asking for randomness

# 1.26 nCk TODO
def combination(l, n, k):
    pass
