class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index):
        if index >= self.size or index < 0:
            return -1
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.val
        
    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def addAtTail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
        
    def addAtIndex(self, index, val):
        new_node = Node(val)
        if index > self.size or index < 0:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1
            
    def deleteAtIndex(self, index):
        if index >= self.size or index < 0:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
