# AVL self balancing tree, where based on the node factor it will fo left shift and right shift

class AVLtree:
    # node_factor should be in the range of -1,0,1
    def __init__(self, data=-1, node_factor=0, left=None, right=None, parent=None, root= None):
        self.data = data
        self.node_factor = node_factor
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.root = root

    def isroot(self):
        return not self.parent

    def put(self, insert_node):
        def put_AVL_helper(curr_root, insert_node):
            if curr_root.data > insert_node:
                if curr_root.left_child == None:
                    curr_root.left_child = AVLtree(insert_node, parent=curr_root)
                    print curr_root.left_child
                    self.check_node_factor(curr_root.left_child)
                else:
                    put_AVL_helper(curr_root.left_child, insert_node)
            else:
                if curr_root.data < insert_node:
                    if curr_root.right_child == None:
                        curr_root.right_child = AVLtree(insert_node, parent=curr_root)
                        self.check_node_factor(curr_root.right_child)
                    else:
                       put_AVL_helper(curr_root.right_child, insert_node)
        put_AVL_helper(self, insert_node)


    def check_node_factor(self, node):
        # check if the node is unbalanced, if it is unbalanced do update
        if node.node_factor > 1 or node.node_factor < -1:
             self.rebalance_factor(node)
             return

        if node.parent != None:
            if node.parent and node.parent.left_child == node:
                node.parent.node_factor += 1
            elif node.parent.right_child == node:
                node.parent.node_factor -=1

            if node.parent.node_factor != 0:
                self.check_node_factor(node.parent)

    # rotate left, if the tree is right heavy
    '''
       The right subtree root will become the new root, The current root will become the new left subtree rootand
       right_subtree left child will become the new left subtree root's right child and the right subtree's right
       child will become the  right subtree root
    '''

    def rotate_left(self, node):
        new_root = node.right_child
        node.right_child = new_root.left_child
        if new_root.left_child != None:
            new_root.left_child.parent = node
        new_root.parent = node.parent
        if node.isroot():
            self.root = new_root
        else:
            if node.parent and node.parent.left_child == node:
                node.parent.left_child = new_root
            else:
                node.parent.right_child = new_root
        new_root.left_child = node
        node.parent = new_root

        node.node_factor = node.node_factor + 1 - min(new_root.node_factor, 0)
        new_root.node_factor = new_root.node_factor + 1 + max(node.node_factor, 0)

    # rotate right, if the left subtree is heavy
    '''
       The left subtree root will become the new root, the cureent root will become the right subtree's root
       left subtree's right child will become the new right subtree root, the left subtree's left child will become
       the new left subtree root.
    '''

    def rotate_right(self, node):

        new_root = node.left_child
        node.left_child = new_root.right_child

        if new_root.right_child != None:
            new_root.right_child.parent = node
        new_root.parent = node.parent

        if node.isroot():
            self.root = new_root
        else:

            if node.parent and node.parent.right_child == node:
                node.parent.right_child = new_root
            else:
                node.parent.left_child = new_root

        new_root.right_child = node
        node.parent = new_root

        node.node_factor = node.node_factor -1 - min(new_root.node_factor, 0)
        new_root.node_factor = new_root.node_factor -1 + max(node.node_factor, 0)
        return new_root.data, new_root.node_factor

    # refactor will call the appropritae rotation based on node factor
    '''
       rebalance_factor will do the rotation based on the node_factor value
    '''
    def rebalance_factor(self, node):
        # right heavy
        if node.node_factor < 0:
            # check if the node_factor is greater than 0, if greater than 0, do right rotation and then left rotation
            if node.right_child.node_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                 self.rotate_left(node)

        #left heavy
        elif node.node_factor > 0:
            # if the node_factor is less than 0, do the left rotation and perform the right rotation
            if node.left_child.node_factor < 0:
                self.rotate_left(node.left_child)
                res = self.rotate_right(node)
                print res
            else:
                 res = self.rotate_right(node)
                 print res

    def print_AVL(self):
        if self.data != -1:
            print "root", self.data
            if self.left_child != None:
                print "left_child", self.left_child.data
                self.left_child.print_AVL()
            if self.right_child != None:
                print "right_child", self.right_child.data
                self.right_child.print_AVL()



A = AVLtree(12, node_factor=0, root=12)
A.put(10)
A.put(5)
A.put(11)
A.put(3)
A.put(8)
A.put(15)

