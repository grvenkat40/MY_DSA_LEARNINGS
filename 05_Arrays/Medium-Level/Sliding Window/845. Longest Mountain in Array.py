class Solution:
    def longestMountain(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        maxi = 0
        i = 1
        while i < n-1:
            if nums[i-1] < nums[i] > nums[i+1]:
                left = i - 1
                right = i + 1

                while left > 0 and nums[left-1] < nums[left]:
                    left -= 1
                
                while right < n-1 and nums[right] > nums[right+1]:
                    right += 1
                
                maxi = max(maxi, right - left + 1)

                i = right
            else:
               i += 1
        return maxi
    
obj = Solution()

print(obj.longestMountain([2,1,4,7,3,2,5]))