class LRUCache:
    class Node:
        def __init__(self,_key,_val):
            self.key = _key
            self.val = _val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):

        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cap = capacity

        self.hash = {}
    
    def addNode(self, newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode
    
    def deleteNode(self, delNode):
        delPrev = delNode.prev
        delnext = delNode.next
        delPrev.next = delnext
        delnext.prev = delPrev

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        recNode = self.hash[key]
        self.deleteNode(recNode)
        self.addNode(recNode)
        return recNode.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            exisitingNode = self.hash[key]
            exisitingNode.val = value
            self.deleteNode(exisitingNode)
            self.addNode(exisitingNode)
            return 

        if len(self.hash) == self.cap:
            lru = self.tail.prev
            del self.hash[lru.key]
            self.deleteNode(lru)
        
        newNode = self.Node(key, value)
        self.hash[key] = newNode
        self.addNode(newNode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)