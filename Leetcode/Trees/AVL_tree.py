'''
AVL tree is a self balancing tree whose left and right will differ by -1/+1

'''

class AVL:
    def __init__(self, data, height = 1 , parent=None, left=None, right=None):
        self.data = data
        self.height = height
        self.left_child = left
        self.right_child = right
        self.parent = parent

    # returns the height of the node
    def get_height(self, node):
        if not node:
            return 0
        else:
            return node.height

    # checks if the left and right is balanced by +1, 0, -1
    def is_balanced(self, node):
        if not node:
            return True

        temp_height_factor = abs(node.left_child.height - node.right_child.height)
        return [temp_height_factor == 0, temp_height_factor]

class AVL_operations(AVL):
    # calls the super class
    def __init__(self, data):
        self.root = AVL.__init__(data)

    '''
    Insert the node, check for the balance factor of it's parents, if <0 left heavy elif >0 right heavy else(==0) balanced
    '''
    def insert(self, root, node_val):
        # create a AVL node
        if not root:
            self.res = AVL(node_val)
        elif root.data > node_val:
            # insert left
            root.left_child = self.insert(root.left_child, node_val)
        else:
            # insert right
            root.right_child = self.insert(root.right_child, node_val)

        # update the height factor to it's ascendant nodes
        root.height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))

        # check for the balance factor, if it is not in the range of -1, 0, +1 then do the rotation
        balanced = self.is_balanced(root)

        if not balanced[0]:
            # left_rotation when balanced < 0
            if balanced[1] > 1 and node_val < root.left_child.data:
                self.rotate_right(root)
            # right rotation when balanced > 0
            elif balanced[1] < -1 and node_val > root.right_child.data:
                self.right_child(root)
            # left-right rotation when the balanced is < 0 and it's right child to the parent
            elif balanced[1] > 1 and node_val > root.leftt_child.data:
                res = self.rotate_left(root)
                self.rotate_right(res)
            # right-left rotation when the balanced is > 0 and it's left child to the parent
            elif balanced[1] < -1 and node_val > root.right_child.data:
                res = self.rotate_right(root)
                self.rotate_left(res)


    '''
    delete the node once found and update it's parents balance factor
    call rotation based on the balance factor
    '''
    def delete_node(self, node_to_delete):
        pass

    '''
    when the node is inseretd on the left subtree and to the left of the parent node, do right rotation
    '''
    def rotate_right(self, node):
        # how to rotate? need node's parent and node's parent's parent and update the balance factor to
        # node's parent's parent's parent
        temp = node.left_child
        temp_rightchild = temp.right_child             # it will become the node's left_child
        #rotate
        temp.right_child = node
        node.right_child = temp_rightchild
        # update height
        temp.height = 1 + max(self.get_height(temp.left_child), self.get_height(temp.left_child))
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))

        return temp

    '''
    when node is inserted to the right subtree's right, to balance do left rotation
    '''
    def rotate_left(self, node):
        # store the node's right
        temp = node.right_child
        temp_leftchild = temp.left_child

        # move the node to temp's left_child
        temp.left_child = node
        node.right_child = temp_leftchild

        # update balance factor
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child.height))
        temp.height = 1 + max(self.get_height(temp.left_child), self.get_height(temp.right_child.height))

        return temp


