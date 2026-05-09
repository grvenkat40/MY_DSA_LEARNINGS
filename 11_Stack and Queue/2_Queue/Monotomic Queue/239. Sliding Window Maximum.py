from collections import deque
class Solution:
    def MY_Solution_maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        ans = nums[:k]
        res.append(max(ans))
        left = 0
        for right in range(k, len(nums)):
            ans.remove(nums[left])
            ans.append(nums[right])
            res.append(max(ans))
            left += 1
        return res

    def Optimal_maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        dq = deque()
        for i in range(len(nums)):
            if dq and dq[0] <= i-k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]])
            
        return res

obj = Solution()
print(obj.MY_Solution_maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(obj.Optimal_maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))