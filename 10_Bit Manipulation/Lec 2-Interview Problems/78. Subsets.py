class Solution:
    def subsets(self, nums) :
        result = []
        subsets = 1 << len(nums) # or 2**len(nums)
        for i in range(subsets):
            ls = []
            for j in range(len(nums)):
                if (i & (1 << j)):
                    ls.append(nums[j])
            result.append(ls)
        return result

obj = Solution()
nums = [1,2,3]
print(obj.subsets(nums))