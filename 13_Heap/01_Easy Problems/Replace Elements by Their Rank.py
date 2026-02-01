import heapq
class Solution:
    def replace_with_rank(self, arr):
        min_heapp = arr.copy()
        heapq.heapify(min_heapp)
        result = {}
        i = 1
        while min_heapp:
            val = heapq.heappop(min_heapp)
            if val not in result:
                result[val] = i 
                i += 1
        res = [result[num] for num in arr]
        return res
obj = Solution()
arr = [20, 15, 26, 2, 98, 6]
print(obj.replace_with_rank(arr))