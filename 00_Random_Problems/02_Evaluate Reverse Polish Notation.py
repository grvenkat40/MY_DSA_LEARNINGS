class Solution:
    def evalRPN(self, tokens) -> int:
        ops={
            '+' : lambda x,y:int(x+y),
            '-' : lambda x,y:int(x-y),
            '*' : lambda x, y:int(x*y),
            '/' : lambda x,y:int(x/y)
        }
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[tokens[i]](b,a))
        return stack[0]
    
obj = Solution()
tokens = ["2","1","+","3","*"]
print(obj.evalRPN(tokens))