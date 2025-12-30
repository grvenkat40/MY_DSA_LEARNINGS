class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def prob(text):
            stack = []
            for c in s:
                if c == "#":
                    if stack:
                        stack.pop()
                        continue
                    else:
                        continue
                else:
                    stack.append(c)
            return "".join(stack)
        
        # stack1 = []
        # for c in t:
        #     if c == "#":
        #         if stack1:
        #             stack1.pop()
        #             continue
        #         else:
        #             continue
        #     else:
        #         stack1.append(c)
        return prob(s) == prob(t)
obj = Solution()
s = "ab#c"
t= "ad#c"
print(obj.backspaceCompare(s, t))