import heapq
class Solution:    
    def kthLargestElement(self, nums, k):
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        return -max_heap[0]
obj = Solution()
nums =  [1, 2, 3, 4, 5]
k = 2
print(obj.kthLargestElement(nums, k))