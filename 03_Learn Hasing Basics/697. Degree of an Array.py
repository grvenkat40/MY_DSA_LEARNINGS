from collections import Counter
import time

class BruteSolution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        hash = Counter(nums)
        maxi = 0
        min_len = float('inf') 
        for v,c in hash.items():
            if c > maxi:
                maxi = c
                # break
                start = 0
                end = 0
                for i in range(len(nums)):
                    if nums[i] == v:
                        start = i
                        break
                for j in range(len(nums)-1, -1, -1):
                    if nums[j] == v:
                        end = j
                        break
                min_len = end - start+1
            elif c == maxi:
                start = 0
                end = 0
                for i in range(len(nums)):
                    if nums[i] == v:
                        start = i
                        break
                for j in range(len(nums)-1, -1, -1):
                    if nums[j] == v:
                        end = j
                        break
                min_len = min(min_len, (end-start+1))
        return min_len


class OptimalSolution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        left = {}
        right = {}
        freq = {}
        for i, val in enumerate(nums):
            if val not in left:
                left[val] = i
            right[val] = i
            freq[val] = freq.get(val, 0)+1
        max_freq = max(freq.values())
        min_len = len(nums)
        for v in freq:
            if freq[v] == max_freq:
                min_len = min(min_len, (right[v] - left[v]+1))
        return min_len


st = time.perf_counter()
obj = BruteSolution()
nums = [1,2,2,3,1,4,2]
print(obj.findShortestSubArray(nums))
end = time.perf_counter()
print(st, end)

start = time.perf_counter()
obj = OptimalSolution()
nums = [1,2,2,3,1,4,2]
print(obj.findShortestSubArray(nums))
ends = time.perf_counter()
print(start, ends)