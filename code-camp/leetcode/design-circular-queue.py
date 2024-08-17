class MyCircularQueue:
    def __init__(self, k : int):
        self.queue = []
        self.k = k
        
    def  enQueue (self, value : int):
        if not self.isFull():
            self.queue.append(value)
            return True
        
    def deQueue (self):
        if not self.isEmpty():
            self.queue.pop(0)
            return True
    
    def isEmpty(self):
        return len(self.queue) == 0
        
    def isFull(self):
        return len(self.queue) == self.k
    
    def Rear(self ):
        if not self.queue:
            return -1
        return self.queue[-1]
    
    def Front(self):
        if not self.queue:
            return -1
        return self.queue[0]
    