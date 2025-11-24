class Solution:   
    def singleNumber(self, nums):
        if len(nums) <= 2:
            return nums
        hash = {}
        for i in nums:
            hash[i] = hash.get(i,0)+1
        result = []
        for i,j in hash.items():
            if j == 1:
                result.append(i)
        return result

obj = Solution()
nums = [1, 2, 1, 3, 5, 2]
print(obj.singleNumber(nums))