import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.mini_heap = nums
        heapq.heapify(nums)
        while len(self.mini_heap) > k:
            heapq.heappop(self.mini_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.mini_heap, val)
        if len(self.mini_heap) > self.k:
            heapq.heappop(self.mini_heap)
        return self.mini_heap[0]

k = 3
nums = [4, 5, 8, 2]
print(nums)
obj = KthLargest(k, nums)
print(nums)
print(obj.add(3))
print(nums)
print(obj.add(5))
print(nums)
print(obj.add(10))
print(nums)
print(obj.add(9))
print(nums)
print(obj.add(4))