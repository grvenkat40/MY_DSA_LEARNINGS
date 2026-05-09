from collections import deque
class Solution:
    def MY_Solution_shortestSubarray(self, nums: list[int], k: int) -> int:
        mini = float("inf")
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= k:
                mini = min(mini, right-left+1)
                total -= nums[left]
                left += 1
        if total >= k:
            mini = min(min, right-left+1)
        return mini if mini != float("inf") else -1
    
    def Optimal_shortestSubarray(self, nums: list[int], k: int) -> int:
        mini = float("inf")
        n = len(nums)
        prefix = [0] * (n+1) 
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        dq = deque()

        for i in range(n+1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                mini = min(mini, i-dq.popleft())
            
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        return mini if mini != float("inf") else -1

    
obj = Solution()
print(obj.MY_Solution_shortestSubarray(nums = [2,-1,2], k = 3))
print(obj.Optimal_shortestSubarray(nums = [2,-1,2], k = 3))
