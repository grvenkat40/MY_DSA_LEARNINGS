class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.cnt = 1
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertNode(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size += 1

    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1

class LFUCache:
    def __init__(self, capacity: int):
        self.maxcap = capacity
        self.leastFreq = 0
        self.currSize = 0

        self.cache = {}
        self.freqList = {}
        
    def updateFreqListMap(self, node):
        freq = node.cnt
        self.freqList[freq].deleteNode(node)

        if freq == self.leastFreq and self.freqList[freq].size == 0:
            self.leastFreq += 1
        
        node.cnt +=1 
        if node.cnt not in self.freqList:
            self.freqList[node.cnt] = DList()

        self.freqList[node.cnt].insertNode(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            self.updateFreqListMap(node)
            return val

        return -1

    def put(self, key: int, value: int) -> None:
        if self.maxcap == 0:
            return 
        
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.updateFreqListMap(node)
        else:
            if self.currSize == self.maxcap:
                listToDelete  = self.freqList[self.leastFreq]
                del self.cache[listToDelete.tail.prev.key]

                self.freqList[self.leastFreq].deleteNode(listToDelete .tail.prev)
                self.currSize -= 1

            self.currSize += 1

            self.leastFreq = 1

            listFreqency = DList()

            if self.leastFreq in self.freqList:
                listFreqency = self.freqList[self.leastFreq]

            node = Node(key, value)

            listFreqency.insertNode(node)

            self.cache[key] = node

            self.freqList[self.leastFreq] = listFreqency


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)