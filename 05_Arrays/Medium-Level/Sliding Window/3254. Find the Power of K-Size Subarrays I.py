class Solution:
    def Brute_resultsArray(self, nums: list[int], k: int) -> list[int]:
        res = []
        n = len(nums)
        sub = nums[:k]
        def is_valid(arr):
            for i in range(1, len(arr)):
                if arr[i] != arr[i-1]+1:
                    return False
            return True
        if is_valid(sub):
            res.append(sub[-1])
        else:
            res.append(-1)
        for i in range(k, n):
            sub.pop(0)
            sub.append(nums[i])
            if is_valid(sub):
                res.append(sub[-1])
            else:
                res.append(-1)
        return res

    def Optimal(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        res = [-1] * (n-k+1)
        for i, val in enumerate(nums):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                res[i-k+1] = val
        return res

obj = Solution()
print(obj.Brute_resultsArray(nums = [1,2,3,4,3,2,5], k = 3))
print(obj.Optimal(nums = [1,2,3,4,3,2,5], k = 3))