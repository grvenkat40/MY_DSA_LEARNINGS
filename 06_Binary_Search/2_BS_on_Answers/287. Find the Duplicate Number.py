class Solution:
    def MySolution_findDuplicate(self, nums: list[int]) -> int:
        hash = {}                                     #Time : O(n)
        for n in nums:                                # Space : O(n)
            hash[n] = hash.get(n, 0) + 1
            if hash[n] > 1:
                return n
            
    def Optimal_findDuplicate(self, nums: list[int]) -> int:
        low = 1                                     
        high = len(nums) - 1                   #Time : O(n)                                                      
                                               # Space : O(1)
        while low < high:
            mid = low + (high - low) // 2
            
            count = sum(1 for num in nums if num <= mid)
            if count > mid:
                high = mid
            else:
                low = mid + 1
                
        return low
    
obj = Solution()
print(obj.MySolution_findDuplicate(nums = [1,3,4,2,2]))
print(obj.Optimal_findDuplicate(nums = [1,3,4,2,2]))