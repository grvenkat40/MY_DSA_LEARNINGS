class BruteSolution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        subarr = []
        accCnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr.append(nums[i:j+1])
        for arr in subarr:
            cnt = 0
            for i in range(len(arr)):
                if arr[i] % 2 ==1:
                    cnt += 1
            if cnt == k:
                accCnt += 1
        return accCnt
    
"""---------------------------------------------------"""

class BetterSolution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        return self.func(nums, k) - self.func(nums, k-1)

    def func(self, nums, k):
        if k < 0:
            return 0
        cnt = 0
        l = 0
        r = 0
        sum = 0
        while r < len(nums):
            sum += (nums[r]%2)
            while sum > k:
                sum -= (nums[l]%2)
                l += 1
            cnt += (r-l+1)
            r += 1
        return cnt
        
"""---------------------------------------"""
class OptimalSolution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        preSum = 0
        prefixCnt = {0:1}
        result = 0
        for i in range(len(nums)):
            preSum += nums[i]%2
            result += prefixCnt.get(preSum-k, 0)
            prefixCnt[preSum] = prefixCnt.get(preSum, 0)+1
        return result
        
obj1 = BruteSolution()
nums = [1,1,2,1,1]
k = 3
print(obj1.numberOfSubarrays(nums, k))

obj2 = BetterSolution()
nums = [1,1,2,1,1]
k = 3
print(obj2.numberOfSubarrays(nums, k))

obj3 = OptimalSolution()
nums = [1,1,2,1,1]
k = 3
print(obj3.numberOfSubarrays(nums, k))