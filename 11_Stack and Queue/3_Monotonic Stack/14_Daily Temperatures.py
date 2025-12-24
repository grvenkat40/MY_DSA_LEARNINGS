#Brute
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ngt = [0]*n
        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    ngt[i] = j-i
                    break
        return ngt

obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(obj.dailyTemperatures(temperatures))

#Optimal
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        ngt = [0]*n
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                ngt[i] = stack[-1][1] - i
            else:
                ngt[i] = 0
            stack.append((temperatures[i],i))
        return ngt

obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(obj.dailyTemperatures(temperatures))