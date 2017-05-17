class Tree:
    def __init__(self, root):
        self.root = root
        self.leftchild = None
        self.rightchid = None

    def get_left_child(self):
        return self.leftchild

    def get_right_child(self):
        return self.rightchid

    def get_root(self):
        return self.root

class ParseTree:
    def __init__(self):
        tree_root = Tree()

    #get the expression and return the tree
    def getExpression(self, exp):
        #1. get the exp and split them and store it into an array
        #2. parse the array list using while loop
             #2.1 if input is '(', then create left node and set it as current node
             #2.2 if input is number insert it under the current node
             #2.2 if input is ')' return to the parent of current node
