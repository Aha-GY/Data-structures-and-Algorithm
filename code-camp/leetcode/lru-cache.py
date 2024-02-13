class Node:
    def __init__(self,val,key):
        self.key, self.val = val,key
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.left , self.right = Node(0,0),Node(0,0)
        self.left.next , self.right.prev = self.right,self.left
        self.cashe ={}
        self.cap = capacity
    def insert(self, node):
        prev , nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.next , node.prev= nxt,prev
    def remove(self,node):
        prev , nxt = node.prev, node.next
        prev.next , nxt.prev = nxt , prev
    def get(self, key: int) -> int:
        if  key in self.cashe:
            self.remove(self.cashe[key])
            self.insert(self.cashe[key])
            return self.cashe[key].val     
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cashe:
            self.remove(self.cashe[key])
        self.cashe[key] = Node(key,value)
        self.insert(self.cashe[key])
        if len(self.cashe) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cashe[lru.key]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)