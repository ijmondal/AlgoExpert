'''
this can be implemente recursively and iteratively
'''
# Worst: Time = O(n) Space = O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
                
# recursive
# Worst: Time = O(n) Space = O(n)
def findClosestValueInBst_recuresive(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper_recuresive(tree,target,closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest # the difference is zero, found the exact target in the BST
        
#iterative
# Worst: Time = O(n) Space = O(1)
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree,target,closest):
    currentNode = tree
    while currentNode is not None:
        
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
    
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

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))  
        
        
print(findClosestValueInBst(r,35))
