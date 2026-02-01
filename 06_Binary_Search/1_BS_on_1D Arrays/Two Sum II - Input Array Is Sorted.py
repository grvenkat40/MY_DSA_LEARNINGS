class Solution:
    def TwoPointer_twoSum(self, numbers: list[int], target: int) ->list[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return (i+1, j+1)
            elif total > target:
                j = j - 1
            elif total < target:
                i = i + 1

    def BinarySearch_twoSum(self, numbers: list[int], target: int) ->list[int]:
        n = len(numbers)
        for i in range(n):
            need = target - numbers[i]
            
            low = i + 1
            high = n - 1
            while low <= high:
                mid =( low+high) // 2
                if need == numbers[mid]:
                    return (low+1, high+1)
                elif need > numbers[mid]:
                    high = mid - 1
                elif need < numbers[mid]:
                    low = mid + 1


obj = Solution()
numbers = [2,7,11,15]
target = 9
print(obj.TwoPointer_twoSum(numbers, target))
print(obj.BinarySearch_twoSum(numbers, target))