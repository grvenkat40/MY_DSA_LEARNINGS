class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ministack:
            self.ministack.append(val)
        else:
            self.ministack.append(min(val, self.ministack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.ministack[-1]


obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)