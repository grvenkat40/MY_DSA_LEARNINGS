class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)
        i = 1
        j = n -2
        while i <= j:
            mid = (i+j)//2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid]:
                i = mid + 1 
            elif arr[mid-1]  > arr[mid]:
                j = mid -1
            elif arr[mid + 1] > arr[mid]:
                i = mid + 1
            elif arr[mid + 1] < arr[mid]:
                j = mid -1

obj = Solution()
arr = [0,10,5,2]
print(obj.peakIndexInMountainArray(arr))