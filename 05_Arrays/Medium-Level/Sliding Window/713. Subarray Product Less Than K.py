class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        cnt = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            cnt += (right-left+1)
        return cnt

obj = Solution()
print(obj.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))