# O(n) Time | O(depth) space
class Node:
    def __init__(self, val):
        self.val = val
        self.left = left
        self.right = right

def insert(root, node):
    if root is None:
        root = node
    else:
        if node.val >= root.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
                
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.value)
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
        