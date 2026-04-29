class Solution:
    def Better_productExceptSelf(self, nums):
        prefix = [1]*len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
    
        suffix = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res
    
    def Optimal_productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        # 🔹 Step 1: Prefix pass
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # 🔹 Step 2: Suffix pass
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

obj = Solution()
print(obj.Better_productExceptSelf(nums = [1,2,3,4]))
print(obj.Optimal_productExceptSelf(nums = [1,2,3,4]))