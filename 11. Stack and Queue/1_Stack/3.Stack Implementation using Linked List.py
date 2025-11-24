class Node:
    def __init__(self, x):
        self.data = x 
        self.next = None
    
class myStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        self.top = temp
        self.count += 1
    
    def pop(self):
        if self.top is None:
            print("Stack is Underflow")
            return -1
        temp = self.top
        self.top = self.top.next
        val = temp.data
        self.count -= 1
        return val
    
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return -1
        return self.top.data
    
    def isEmpty(self):
        return self.top is None
    
    def size(self):
        return self.count

if __name__ == "__main__":
    stack = myStack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5) 

    print("Popped", stack.pop())

    print("Peek Element", stack.peek())

    print("Is stack is Empty", 'Yes' if stack.isEmpty() else "No")

    print("Size", stack.size())
