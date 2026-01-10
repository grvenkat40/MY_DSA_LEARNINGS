class Solution:
    def waysToMakeFair(self, nums:list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            arr = nums.copy()
            arr.pop(i)
            preodd = [0]
            preeven = [0]
            for j, n in enumerate(arr):
                if j%2 == 0:
                    preeven.append(preeven[-1] + n)
                else:
                    preodd.append(preodd[-1] + n)
            if preodd[-1] == preeven[-1]:
                result += 1
        return result
obj = Solution()
nums = [4,1,1,2,5,1,5,4]
print(obj.waysToMakeFair(nums))