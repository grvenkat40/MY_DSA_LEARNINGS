class Solution:
    def Brute_sumSubarrayMins(self, arr) -> int:
        subarr = []
        total = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                total += min(arr[i:j+1])
        return total
    
    """--------------------------------------------------------------------------------------"""

    def optimal_sumSubarrayMins(self, arr):
        mod = int(10**9+7)
        total = 0
        nse = self.nextSmallerEle(arr)
        psee = self.prevSmallerEqualEle(arr)
        for i in range(len(arr)):
            left = i - psee[i]
            right = nse[i] - i
            total = (total + (right*left*arr[i]%mod))%mod
        return total

    def prevSmallerEqualEle(self, arr):
        n = len(arr)
        psee = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                psee[i] = stack[-1]
            else:
                psee[i] = n
            stack.append(i)
        return psee
    
    def nextSmallerEle(self, arr):
        n = len(arr)
        nse = [0]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            else:
                nse[i] = -1
            stack.append(i)
        return nse

obj = Solution()
arr = [3,1,2,4]
print(obj.Brute_sumSubarrayMins(arr))
arr = [3,1,2,4]
print(obj.optimal_sumSubarrayMins(arr))