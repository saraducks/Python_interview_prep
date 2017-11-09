'''
Given a root node of two binary tree find is they are symmetric
1. get the root node and check if they both are equal if not return
2.
'''
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_symmetric(root_1, root_2):

    if not root_1 and not root_2:
        return  True
    elif root_1 and root_2:
        print(root_1.data, root_2.data)
        return (root_1.data == root_2.data and find_symmetric(root_1.left, root_2.left) and find_symmetric(root_1.right, root_2.right))

    return False


t1 = Tree(data = 12)
t1.left = Tree(data = 14)
t1.left.right = Tree(data = 34)
t1.right = Tree(data = 90)
t1.right.left = Tree(data = 78)
t1.left.left = Tree(data = 56)
t1.right.left.right = Tree(data = 36)


t2 = Tree(12)
t2.left = Tree(data = 14)
t2.left.right = Tree(data = 34)
t2.right = Tree(data = 90)
t2.right.left = Tree(data = 78)
t2.left.left = Tree(data = 56)
t2.right.left.right = Tree(data = 36)


result = find_symmetric(t1, t2)
print(result)