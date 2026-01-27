import heapq
class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        arr = []
        for n in nums:
            val = int(n)
            heapq.heappush(arr,val)
            if len(arr) > k:
                heapq.heappop(arr)
        return str(arr[0])

obj =Solution()
nums = ["3","6","7","10"]
k = 4
print(obj.kthLargestNumber(nums, k))