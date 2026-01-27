import heapq
class Solution:
    def kthLargestElement(self, nums: list[int], k: int) -> int:
        min_heap = nums
        heapq.heapify(min_heap)
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        return min_heap[0]

obj = Solution()
nums =  [1, 2, 3, 4, 5]
k = 2
print(obj.kthLargestElement(nums, k))