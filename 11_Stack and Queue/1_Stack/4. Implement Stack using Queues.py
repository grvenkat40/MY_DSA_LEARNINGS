from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def empty(self) -> bool:
        return len(self.stack) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)