'''
AVL tree is a self balancing tree whose left and right will differ by -1/+1

'''

class AVL:
    def __init__(self, data=None, height=None, parent=None, left=None, right=None):
        self.data = data
        self.height = height
        self.left_child = left
        self.right_child = right
        self.parent = parent

    # returns the height of the node
    def get_height(self):
        return self.height

    # checks if the left and right is balanced by +1, 0, -1
    def is_balanced(self):
        temp_height_factor = abs(self.left_child.height - self.right_child.height)
        return (temp_height_factor == 0 )

class AVL_operations(AVL):

    '''
    Insert the node, check for the balance factor of it's parents, if <0 left heavy elif >0 right heavy else(==0) balanced
    '''
    def insert(self, node_val):
        pass

    '''
    delete the node once found and update it's parents balance factor
    call rotation based on the balance factor
    '''
    def delete_node(self, node_to_delete):
        pass

    '''
    when the node is inseretd on the left subtree and to the left of the parent node, do right rotation
    '''
    def rotate_right(self):
        # how to rotate? need node's parent and node's parent's parent and update the balance factor to
        # node's parent's parent's parent
        pass

    '''
    when node is inserted to the right subtree's right, to balance do left rotation
    '''
    def rotate_left(self):
        pass

    '''
    when the node is inserted to the right subtree of the left subtree, do left and then right rotation
    '''
    def rotate_leftright(self):
        pass

    '''
    when the node is insrted to the left subtree of the right subtree
    '''
    def rotate_rightleft(self):
        pass

