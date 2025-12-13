class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        def find(k):
            l=r=cnt = 0
            hash = {}
            while r < len(nums):
                hash[nums[r]] = hash.get(nums[r], 0)+1
                while len(hash) > k:
                    hash[nums[l]] -= 1
                    if hash[nums[l]] == 0:
                        del hash[nums[l]]
                    l += 1
                if len(hash) <= k:
                    cnt += (r-l+1)
                r += 1
            return cnt
        return find(k) - find(k-1)
    

obj = Solution()
nums = [1,2,1,2,3]
k = 2
print(obj.subarraysWithKDistinct(nums, k))