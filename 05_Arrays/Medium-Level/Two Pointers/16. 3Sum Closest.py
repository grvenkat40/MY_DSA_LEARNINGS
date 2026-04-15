class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans = float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - ans):
                    ans = total 
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return ans

obj = Solution()
print(obj.threeSumClosest(nums = [-1,2,1,-4], target = 1))