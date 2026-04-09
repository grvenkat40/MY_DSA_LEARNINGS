class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        maxi = 0
        for i in range(len(nums)-1, -1, -1):
            diff = nums[i] - nums[i-1]
            maxi = max(maxi, diff)
        return maxi

obj = Solution()
print(obj.maximumGap(nums = [3,6,9,1]))