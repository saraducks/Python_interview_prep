class BST:
    def __init__(self, data, left_child=None, right_child=None):
        self.node_value = data
        self.left_child = left_child
        self.right_child = right_child

    def put(self, input_data):
        if input_data.node_value < self.node_value:
            self.left_child = input_data
        elif input_data.node_value > self.node_value:
            self.right_child = input_data

    def print_tree(self):
            print "root", self.node_value
            if self.left_child == None:
                print "left", self.left_child.node_value
            if self.right_child == None:
                print "right", self.right_child.node_value


B = BST(10)
B1 = BST(12)
B2 = BST(3)
B3 = BST(5)
B.put(B1)
B.put(B2)
B.put(B3)
B.print_tree()
