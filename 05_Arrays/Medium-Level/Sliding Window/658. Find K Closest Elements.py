class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l = 0
        r = len(arr)-1
        while (r - l + 1) > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l:r+1]   

obj = Solution()
print(obj.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))