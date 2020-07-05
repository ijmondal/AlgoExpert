class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
def insert(root, node):
    if root is None:
        root = node
    else: 
        if root.val < node.val: #right subtree
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else: #left subtree
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# T = O(n) | S = O(n)
def invertBT_iterative(root):
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current is None:
            continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)

# T = O(n) | S = O(logn) or O(depth)
def invertBT_recursive(root):
    if root is None:
        return
    else:
        root.left, root.right = root.right, root.left
        invertBT_recursive(root.left)
        invertBT_recursive(root.right)


        
  
            
              
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))  
inorder(r)
print("\n")
invertBT_recursive(r)
inorder(r)