from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash = Counter(nums)
        ls = sorted(hash.items(),key = lambda x:x[1], reverse = True)
        return [x[0] for x in ls[:k]]
    
obj = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(obj.topKFrequent(nums, k))