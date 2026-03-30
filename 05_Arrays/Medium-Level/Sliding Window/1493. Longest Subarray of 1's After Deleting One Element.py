class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxi = 0
        nZore = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                nZore += 1
            while nZore > 1:
                if nums[i] == 0:
                    nZore -= 1
                i += 1
            maxi = max(maxi, j-i)
        return maxi
        
obj = Solution()
print(obj.longestSubarray(nums = [0,1,1,1,0,1,1,0,1]))