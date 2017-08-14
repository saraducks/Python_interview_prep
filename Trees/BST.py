class BST:
    def __init__(self, data=-1, left_child=None, right_child=None):
        self.node_value = data
        self.left_child = left_child
        self.right_child = right_child

    def put(self, input_data):
        def put_helper(node, input_data):
            # check if the left child is None
            if input_data.node_value < node.node_value:
                if node.left_child == None:
                    node.left_child = input_data
                    print node.left_child.node_value
                else:
                    put_helper(node.left_child, input_data)
            elif input_data.node_value > node.node_value:
                if node.right_child == None:
                     node.right_child = input_data
                     print node.right_child.node_value
                else:
                    put_helper(node.right_child, input_data)
        put_helper(self, input_data)

    def print_tree(self):
        if self.node_value != -1:
            print "root", self.node_value

            if self.left_child != None:
                print "left", self.left_child.node_value
                self.left_child.print_tree()

            if self.right_child != None:
                print "right", self.right_child.node_value
                self.right_child.print_tree()




B = BST(10)
B1 = BST(12)
B2 = BST(3)
B3 = BST(5)
B.put(B1)
B.put(B2)
B.put(B3)
B.print_tree()
