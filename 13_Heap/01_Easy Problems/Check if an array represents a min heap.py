class Solution:
    def isHeap(self, nums):
        n = len(nums)
        # Iterate through all non-leaf nodes
        for i in range(n//2):
            left = 2*i+1
            if left < n and nums[i] > nums[left]:
                return False
            right = 2*i+2
            if right < n and nums[i] > nums[right]:
                return False
        return True

obj = Solution()
nums = [10, 20, 30, 21, 23]
print(obj.isHeap(nums))