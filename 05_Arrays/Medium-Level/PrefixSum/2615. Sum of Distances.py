from collections import defaultdict
class Solution:
    def Brute_distance(self, nums: list[int]) -> list[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    res[i] += abs(i-j)
        return res
    
    def Optimal_distance(self, nums):
        
obj = Solution()
print(obj.Brute_distance(nums = [1,3,1,1,2]))
print(obj.Optimal_distance(nums = [1,3,1,1,2]))