class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
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
        
def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value > maxValue:
        return False
    leftIsValid = validateBSTHelper(tree.left, minValue, tree.value)
    rightIsValid = validateBSTHelper(tree.right, tree.value, maxValue)
    return leftIsValid and rightIsValid

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

print(validateBST(r)) 