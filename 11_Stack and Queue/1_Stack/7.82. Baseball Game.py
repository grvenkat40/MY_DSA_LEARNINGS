class Solution:
    def calPoints(self, operations: list[str]) -> int:
        # res = []
        stack = []
        for n in operations:
            if n == "+":
                stack.append(stack[-1]+stack[-2])
            elif n == "C":
                stack.pop()
            elif n == "D":
                stack.append(2*stack[-1])
            else:
                stack.append(int(n))
        return sum(stack)
obj = Solution()
ops = ["5","2","C","D","+"]
print(obj.calPoints(ops))