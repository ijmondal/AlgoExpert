'''
## Linked List Construction

#### Problem Statement


Write a class for a Doubly Linked List. The class should have a "head" and "tail" properties, both of which should point to either the None (null) value or to a
Linked List node. Every node will have a "value" property as well as "next" and "prev" properties, both of which can point to either the None (null) value or
another node. The class should support setting the head and tail of the linked list, inserting nodes before and after other nodes as well as at certain positions,
removing given nodes and removing nodes with specic values, and searching for nodes with values. Only the searching method should return a value:
specically, a boolean.


Sample input:
1 -> 2 -> 3 -> 4 -> 5
Sample output (after setting 4 to head):
4 -> 1 -> 2 -> 3 -> 5
Sample output (after setting 6 to tail):
4 -> 1 -> 2 -> 3 -> 5 -> 6
Sample output (after inserting 3 before 6):
4 -> 1 -> 2 -> 5 -> 3 -> 6
Sample output (after inserting a new 3 after 6):
4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
Sample output (after inserting a new 3 at position 1):
3 -> 4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
Sample output (after removing nodes with value 3):
4 -> 1 -> 2 -> 5 -> 6
Sample output (after removing 2):
4 -> 1 -> 5 -> 6
Sample output (after searching for 5): True
'''
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


     # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node) #corner case -- setting new head 
        
     # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)


    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        #edge case
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert) #if the node exists in the linked list we will remove it. This step can be skipped
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert


     # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert) #if the node exists in the linked list we will remove it. This step can be skipped
        nodeToInsert.prev=node
        nodeToInsert.next = node.next
        if node.next == None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert


    # O(Position) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)
        
    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            #we need this temp variable because we are losing node.next in removeNodeBindinnodegs()
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)


    # O(1) time | O(1) space
    def remove(self, node):
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
        #checks if we are removing head or tail and updating new head or tail
        self.removeNodeBindings(node)


    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None  

    def removeNodeBindinnodegs(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
        
class node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

