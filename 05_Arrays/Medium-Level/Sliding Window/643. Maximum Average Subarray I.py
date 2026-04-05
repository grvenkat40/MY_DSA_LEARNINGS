class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i = 0
        res = sum(nums[:k])
        ans = res
        for j in range(k,len(nums)):
            ans += nums[j]
            ans -= nums[i]
            res = max(res, ans)
            i += 1
        return res/k

obj = Solution()
print(obj.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))