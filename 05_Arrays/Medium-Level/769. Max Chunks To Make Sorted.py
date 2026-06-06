class Solution:
    def maxChunksToSorted(self, arr) -> int:
        max_so_for = 0
        chunk = 0
        for i in range(len(arr)):
            max_so_for = max(max_so_for, arr[i])
            if max_so_for == i:
                chunk += 1
        return chunk

obj = Solution()
print(obj.maxChunksToSorted(arr = [1,0,2,3,4]))