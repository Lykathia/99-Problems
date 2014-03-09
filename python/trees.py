#!/usr/bin/env python

class tree():

    def __init__(self, value=None, left=None, right=None):
        self.v = value
        self.l = left
        self.r = right

    def __repr__(self):
        return '{}: ({} | {})'.format(self.v, str(self.l), str(self.r))

# 4.01 -- SKIP: all our trees will be binary trees

# 4.02 Construct Balanced BST
def bal_tree(n):
    if n == 0:
        return None
    q = int((n-1)/2)
    r = (n-1)%2
    return [tree('x', bal_tree(i), bal_tree(n-i-1)) for i in range(q, (q+r+1))]

# Should generate all versions of said tree
#print(bal_tree(1))
#print(bal_tree(2))
#print(bal_tree(3))
#print(bal_tree(4))

# 4.03 Symmetic Trees
def is_symmetric(t):
    if t is None:
        return False
    if t.l == None and t.r == None:
        return True
    return is_symmetric(t.l) and is_symmetric(t.r)

assert(True == is_symmetric(tree('x', tree(), tree())))
assert(True == is_symmetric(tree('x', tree('x', tree(), tree()), tree('x', tree(), tree()))))
assert(False == is_symmetric(tree('x', tree())))
assert(False == is_symmetric(tree('x', tree('x', tree(), tree()), tree('x', tree()))))


# 4.08 Count Leaves
def num_leaves(t):
    if t is None:
        return 0
    elif t.l is None and t.r is None:
        return 1
    else:
        return num_leaves(t.l) + num_leaves(t.r)

assert(1 == num_leaves(tree('x', tree('x'))))
assert(1 == num_leaves(tree('x')))
assert(2 == num_leaves(tree('x', tree('x', tree()), tree('x', None, tree()))))

# 4.09 Collect Leaves
def leaves(t):
    if t is None:
        return []
    elif t.l is None and t.r is None:
        return [t]

    return leaves(t.l) + leaves(t.r)

#print(leaves(tree('x')))
#print(leaves(tree('x', tree())))
#print(leaves(tree('x', tree('x', tree(1), tree(2)), tree('a'))))
