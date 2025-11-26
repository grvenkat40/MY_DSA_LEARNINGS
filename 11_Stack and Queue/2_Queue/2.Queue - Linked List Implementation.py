class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
    
class myQueue:
    def __init__(self):
        self.curSize = 0
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.front is None and self.rear is None : 
            self.front = self.rear = new_node
        self.rear.next = new_node
        self.rear = new_node
        self.curSize += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return 
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.curSize -= 1

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        return self.front.data

    def rearr(self):
        if self.isEmpty():
            print("Queue is Empty")
        return self.rear.data

    def size(self):
        return self.curSize

if __name__ == "__main__":
    q = myQueue()
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Dequeue", q.dequeue())

    q.enqueue(40)

    print("Front", q.peek())

    print("Rear", q.rearr())

    print("Size", q.size())
    