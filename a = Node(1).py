class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
    def Linkedlist(self , val):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        a.next =b
        b.next =c
        # x = None
        x =a
        arr =[]
        while x:
            arr.append(x.value())
            x.next
        return arr
        print(arr)
