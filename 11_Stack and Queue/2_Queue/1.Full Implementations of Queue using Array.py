class myQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, x):
        if self.isFull():
            print("Queue is full")
            return 
        self.arr[self.size] = x
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        for i in range(self.size-1):
            self.arr[i-1] = self.arr[i]
        self.size -= 1

    def getFront(self):
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        return self.arr[0]
    
    def getRear(self):
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        return self.arr[self.size-1]
    
if __name__ == '__main__':
    q = myQueue(3)
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Front:", q.getFront())  
    
    q.dequeue()
    print("Front:", q.getFront())  
    print("Rear:", q.getRear())  
    
    q.enqueue(40)
