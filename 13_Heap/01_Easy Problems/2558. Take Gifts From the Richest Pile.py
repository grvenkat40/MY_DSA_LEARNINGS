import heapq
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-n for n in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            n = -heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(math.sqrt(n)))
        return -sum(gifts)

obj = Solution()
gifts = [25,64,9,4,100]
k = 4
print(obj.pickGifts(gifts, k))