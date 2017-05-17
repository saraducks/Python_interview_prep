
class Tree:
    def __init__(self, root = None):
        self.root = root
        self.leftchild = None
        self.rightchid = None

    def get_left_child(self):
        return self.leftchild

    def get_right_child(self):
        return self.rightchid

    def get_root(self):
        return self.root

    def insert_left(self, leftnode):
        if self.leftchild == None:
            self.leftchild =  leftnode

    def insert_right(self, rightnode):
        if self.rightchid == None:
            self.rightchid = rightnode

    def set_root(self, value):
        if self.root == None:
            self.root = value

class ParseTree:
    def __init__(self):
        self.tree_root = Tree()

    #get the expression and return the tree
    def getExpression(self, exp):
        #1. get the exp and split them and store it into an array
        splitexpr = exp.split(' ')
        print(splitexpr)
        #initailize the stack to trace the path
        Pstack = []
        counter = 0
        #2. parse the array list using while loop
        while counter < len(splitexpr):
             #2.1 if input is '(', then create left node and set it as current node
             if splitexpr[counter] == '(':
                 print(splitexpr[counter])
                 Pstack.append(self.tree_root)
                 self.tree_root = self.tree_root.leftchild
             #2.2 if input is number insert it under the current node
             elif splitexpr[counter] not in ['+','-','*','/',')']:
                 print(splitexpr[counter])
                 self.tree_root.set_root(int(splitexpr[counter]))
                 Pstack.pop()
             #2.2 if input is ')' return to the parent of current node
             elif splitexpr[counter] in ['+','-','*','/']:
                 print(splitexpr[counter])
                 self.tree_root.set_root(int(splitexpr[counter]))
                 Pstack.append(self.tree_root)
                 self.tree_root = self.tree_root.rightchild
             elif splitexpr[counter] == ')':
                 print(splitexpr[counter])
                 self.tree_root = ParseTree.pop()
             else:
                 raise ValueError
             counter = counter + 1
        return self.tree_root


P = ParseTree()
i = '( 2 * 6 )'
P.getExpression(i)
