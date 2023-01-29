class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={} #To store key to Node
        #left point to least Recently used node
        #right point to most Recently used node
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self,node):
        #To remove that node from Double Linked List
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
        
    def add(self,node):
        #To add that node in Double Linked List to Right Side 
        prev=self.right.prev
        node.next=self.right
        node.prev=prev
        prev.next=node
        self.right.prev=node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.add(self.cache[key])
        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)