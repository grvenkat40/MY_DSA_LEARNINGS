class myStack:
    def __init__(self, cap):
        self.arr = [0] * cap
        self.capacity = cap
        self.top = -1
    
    #Push operation
    def push(self, x):
        if self.top == self.capacity-1:
            print("Stack Overflow")
            return
        self.top +=1
        self.arr[self.top] = x
    
    #Pop operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        value = self.arr[self.top]
        self.top -= 1
        return value
    
    #Peek (top) element
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        return self.arr[self.top]
    
    #Check if stack is empty
    def isEmpty(self):
        return self.top == -1
    
    #Check if stack is full
    def isFull(self):
        return self.top == self.capacity-1

if __name__ == "__main__":
    stack = myStack(5)

    # pushing elements
    stack.push(1)
    stack.push(2)    
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print("Elements are pushed into the stack")

    # popping one element
    print("Poppend", stack.pop())

    # checking top element
    print("Top element", stack.peek())

    #checking stack isEmpty
    print("Is empty stack", "Yes" if stack.isEmpty() else "No")

    #Check if stack isFull
    print("Is Stack is full", "Yes" if stack.isFull() else "No")