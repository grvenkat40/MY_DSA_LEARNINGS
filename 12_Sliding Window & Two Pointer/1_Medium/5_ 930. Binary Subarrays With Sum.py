class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
               
        return self.func(nums, goal) - self.func(nums,goal-1)

    def func(self,nums, goal):
        if goal < 0:
            return 0
        cnt = 0
        l = 0
        r = 0
        sum = 0
        n = len(nums)
        while r < n:
            sum += nums[r]
            while sum > goal:
                sum -= nums[l]
                l += 1
            cnt += (r-l+1)
            r += 1
        return cnt 

obj1 = Solution()
nums = [1,0,1,0,1]
goal = 2
print(obj1.numSubarraysWithSum(nums, goal))