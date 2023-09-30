# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time, O(1) space
    def addFirstNode(self, node):
        print("running addFirstNode with {}".format(node.value))
        self.head = node
        self.tail = node
    
    # O(1) time, O(1) space
    def setHead(self, node):
        print("running setHead with {}".format(node.value))
        if self.head == None:
            self.addFirstNode(node)
            return
        self.remove(node)
        node.next = self.head
        self.head.prev = node
        self.head = node

    # O(1) time, O(1) space
    def setTail(self, node):
        print("running setTail with {}".format(node.value))
        if self.head == None:
            self.addFirstNode(node)
            return
        self.remove(node)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    # O(1) time, O(1) space
    def insertBefore(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        print("running insertBefore with node: {} and nodeToInsert {}".format(node.value,nodeToInsert.value))
        if node == self.head:
            self.setHead(nodeToInsert)
            return
        # Should be at least one node before node
        prev = node.prev
        prev.next = nodeToInsert
        node.prev = nodeToInsert
        nodeToInsert.next = node
        nodeToInsert.prev = prev

    # O(1) time, O(1) space
    def insertAfter(self, node, nodeToInsert):
        print("running insertAfter with node: {} and nodeToInsert {}".format(node.value,nodeToInsert.value))
        self.remove(nodeToInsert)
        if node == self.tail:
            self.setTail(nodeToInsert)
            return
        next = node.next
        next.prev = nodeToInsert
        node.next = nodeToInsert
        nodeToInsert.prev = node
        nodeToInsert.next = next

    # O(n) time, O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        print("running insertAtPosition with position: {} and nodeToInsert {}".format(position,nodeToInsert.value))
        current = self.head
        for i in range(position-1):
            current = current.next
        if current == self.head:
            self.setHead(nodeToInsert)
        elif current == None:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(current,nodeToInsert)

    # O(n) time, O(n) space
    def removeNodesWithValue(self, value):
        nodesToRemove = []
        current = self.head
        while current != None:
            if current.value == value:
                nodesToRemove.append(current)
            current = current.next
        for node in nodesToRemove:
            self.remove(node)

    # O(1) time, O(1) space
    def remove(self, node):
        if node == self.head and node == self.tail: # Length 1 list
            self.head = None
            self.tail = None
        elif node == self.head: # Removing head
            next = self.head.next
            next.prev = None
            self.head.next = None
            self.head = next
        elif node == self.tail: # Removing head
            prev = self.tail.prev
            prev.next = None
            self.tail.prev = None
            self.tail = prev
        elif node.next == None and node.prev == None:
            return
        else:
            next = node.next
            prev = node.prev
            prev.next = next
            next.prev = prev
            node.prev = None
            node.next = None

    # O(n) time, O(1) space
    def containsNodeWithValue(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False
