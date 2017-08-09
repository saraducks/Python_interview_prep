#!/usr/bin/env python
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

    def insert_left(self, leftnode):
        if self.leftchild == None:
            self.leftchild =  leftnode

    def insert_right(self, rightnode):
        if self.rightchid == None:
            self.rightchid = rightnode

    def set_root(self, value):
            self.root=value

class ParseTree:
    #get the expression and return the tree
    def getExpression(self, exp):
        #1. get the exp and split them and store it into an array
        splitexpr = exp.split(' ')
        print(splitexpr)
        #initailize the stack to trace the path
        Pstack = []
        tree_root = Tree('')
        Pstack.append(tree_root)
        counter = 0
        #2. parse the array list using while loop
        for iter in splitexpr:
             #2.1 if input is '(', then create left node and set it as current node
             if iter == '(':
                 print(iter)
                 tree_root.insert_left('')
                 Pstack.append(tree_root)
                 tree_root = tree_root.get_left_child()
             #2.2 if input is number insert it under the current node
             elif iter not in ['+','-','*','/',')']:
                 print(iter)
                 tree_root.set_root(iter)
                 temp = Pstack.pop()
                 print(temp)
                 tree_root = temp
             #2.2 if input is ')' return to the parent of current node
             elif iter in ['+','-','*','/']:
                 print(iter)
                 tree_root.insert_right('')
                 tree_root.set_root(iter)
                 Pstack.append(tree_root)
                 tree_root = tree_root.get_right_child()
             elif iter == ')':
                 print(iter)
                 tree_root = ParseTree.pop()
             else:
                 raise ValueError
        return tree_root

    # #print tree in preorder
    # def preorder(self):
    #     #traverse left
    #     #traverse right
    #     #visit root
    #
    # #postorder
    # def postorder(self):
    #     #visit root
    #     #traverse left
    #     #traverse right
    #
    # #inorder
    # def inorder(self):
    #     # traverse left
    #     #visit root
    #     # traverse right




P = ParseTree()
i = '( 2 * 6 )'
P.getExpression(i)
