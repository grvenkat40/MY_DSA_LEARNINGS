class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        seen = [False]*(n+1)
        for num in nums:
            if 0 < num <= n:
                seen[num] = True
        for i in range(1, n+1):
            if not seen[i]:
                return i
        return n+1
obj = Solution()
nums = [3,4,-1,1]
print(obj.firstMissingPositive(nums))