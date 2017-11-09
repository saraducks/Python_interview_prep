class BST:
    def __init__(self, val=None, left_child=None, right_child=None):
        self.val = val
        self.left = left_child
        self.right = right_child

    def insert(self, root, node):
        if root is None:
            root =  BST(val = node)
        elif root.val > node:
            root.left = self.insert(root.left, node)
        elif root.val < node:
            root.right = self.insert(root.right, node)

        return root
    '''
    case 1: leaf node, easy to delete
    case 2: if one child then add the child node to curr_node's ancestor
    case 3: if node has both children get the max_value from left child
    '''
    def delete_node(self, root, node_to_delete):
        if not root:
            return root
        elif root.val > node_to_delete:
            root.left = self.delete_node(root.left, node_to_delete)
        elif root.val < node_to_delete:
            root.right = self.delete_node(root.right, node_to_delete)
        else:
            # case1 no child
            if not root.left and not root.right:
                print("leaf node")
                del root
                root = None
            # only left child
            elif root.left and not root.right:
                print("left but not right")
                temp = root
                root = root.left
                del temp
            # only right child
            elif not root.left and root.right:
                print("not left but right")
                temp = root
                root = root.right
                del temp
            # both left and right child
            else:
                print("left and right")
                max_node =  self.find_max_node(root.left)
                print(max_node.val)
                root.val = max_node.val
                root.left = self.delete_node(root.left, max_node.val)

        return root


    '''
    get the maximum value node, in BST it is always the right subtree of the given_node
    
    '''
    def find_max_node(self, curr_root):
        if curr_root.right:
            curr_root = self.find_max_node(curr_root.right)

        return curr_root

    '''
    in order traversal
    '''
    def inorder_traverse(self, root):
        if root:
            self.inorder_traverse(root.left)
            print(root.val)
            self.inorder_traverse(root.right)


# test BST class

root_node = BST()

root = None

root = root_node.insert(root, 100)
root = root_node.insert(root, 120)
root = root_node.insert(root, 56)
root = root_node.insert(root, 67)
root = root_node.insert(root, 65)
root = root_node.insert(root, 66)
root = root_node.insert(root, 89)
root = root_node.insert(root, 560)
root = root_node.insert(root, 600)
root = root_node.insert(root, 780)
root = root_node.insert(root, 10)

# print thr BST
root_node.inorder_traverse(root)
print("_________________________")
result = root_node.delete_node(root, 67)

root_node.inorder_traverse(result)



