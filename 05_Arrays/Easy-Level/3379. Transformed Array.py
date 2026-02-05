class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        result = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                targetInd = i+nums[i]
                if targetInd >= len(nums):
                    ind = targetInd % len(nums)
                    result[i] = nums[ind]
                else:
                    result[i] = nums[targetInd]
            elif nums[i] < 0:
                targetInd = i + nums[i]
                if targetInd < 0:
                    ind = targetInd % len(nums)
                    result[i] = nums[ind]
                else:
                    result[i] = nums[targetInd]
            else:
                result[i] = nums[i]
        return result
obj = Solution()
nums = [3,-2,1,1]
print(obj.constructTransformedArray(nums))