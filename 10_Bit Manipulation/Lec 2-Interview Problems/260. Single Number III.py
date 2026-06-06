from collections import Counter
class Solution:
    def singleNumberMySolution(self, nums):
        if len(nums) <= 2:
            return nums
        hash = Counter(nums)
        res = []
        for key, value in hash.items():
            if value == 1:
                res.append(key)
        return res
    
    def singleNumberOptimalSolution(self, nums):
        xor_all = 0
        for num in nums:
            xor_all ^= num
        diff_bit = xor_all & -(xor_all)
        num1 = 0
        num2 = 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
        
obj = Solution()
print(obj.singleNumberMySolution(nums = [1,2,1,3,2,5]))
print(obj.singleNumberOptimalSolution(nums = [1,2,1,3,2,5]))