class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        hash = {}
        ans = float("inf")
        for i in range(len(nums)):
            if nums[i] in hash:
                ans = min(ans, i - hash[nums[i]])
                hash[int(str(nums[i])[::-1])] = i
            else:
                hash[int(str(nums[i])[::-1])] = i
        return ans if ans != float("inf") else -1

obj = Solution()
print(obj.minMirrorPairDistance(nums = [12,21,45,33,54]))