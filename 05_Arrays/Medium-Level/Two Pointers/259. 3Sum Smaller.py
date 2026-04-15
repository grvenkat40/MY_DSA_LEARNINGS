class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    res += (right-left)
                    left += 1
                else:
                    right -= 1
        return res

obj = Solution()
print(obj.threeSumSmaller(nums= [-2, 0, 1, 3], target= 2))