class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k > 0 and  ord(stack[-1]) > ord(num[i]):
                stack.pop()
                k -= 1
            stack.append(num[i])

        while stack and k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")
        return result if result else "0"

obj = Solution()        
num = "1432219"
k = 3
print(obj.removeKdigits(num , k))