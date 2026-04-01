class Solution:
    def minSubArrayLen(self, target: int, nums:list[int]) -> int:
        mini = float('inf')
        i = 0
        j = 0
        window = 0
        while j < len(nums):
            window += nums[j]
            while window >= target:
                mini = min(mini, j-i+1)
                window -= nums[i]
                i += 1
            j += 1
        return mini if mini != float('inf') else 0

obj = Solution()

print(obj.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))