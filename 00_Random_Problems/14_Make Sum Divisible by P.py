class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        preRem = [0]
        for n in nums:
            preRem.append((preRem[-1]+n) % p)
        hash = {0:-1}
        result = len(nums)
        for i, curr in enumerate(preRem):
            need = (curr - target) % p
            if need in hash:
                result = min(result, i-hash[need])
            hash[curr] = i
        return -1 if len(nums) == result else result
        # return preRem

obj = Solution()
nums = [3,1,4,2]
p = 6
print(obj.minSubarray(nums, p))