class myStack:
    def __init__(self):
        self.arr = []
    
    #Push operation
    def push(self, x):
        self.arr.append(x)

    # pop operation
    def pop(self):
        if not self.arr:
            print("Stack Underflow")
            return -1
        return self.arr.pop()
    
    # peek operation
    def peek(self):
        if not self.arr:
            print("Stack is Empty")
            return -1
        return self.arr[-1]

    # check if stack is empty
    def isEmpty(self):
        return len(self.arr) == 0
    
    # current size
    def size(self):
        return len(self.arr)
   
if __name__ == "__main__":
    st = myStack()

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")

    # checking current size
    print("Current size:", st.size())