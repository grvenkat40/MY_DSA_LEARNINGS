class BruteSolution:
    def longestOnes(self, nums, k: int) -> int:
        maxLen = 0
        for i in range(len(nums)):
            zeros = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    zeros += 1
                if zeros <= k:
                    l = j-i+1
                    maxLen = max(maxLen, l)
                else:
                    break
        return maxLen


"""------------------------------------------------------------------------------------"""

class OptimalSolution:
    def longestOnes(self, nums, k: int) -> int:
        maxLen = 0
        n = len(nums)
        l = 0 
        r = 0
        zeros = 0
        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros <= k:
                cnt = r-l+1
                maxLen = max(maxLen, cnt)
            else:
                while zeros > k:
                    if nums[l] == 1:
                        l += 1
                    else:
                        zeros -= 1
                        l += 1
            r += 1
        return maxLen
        

obj1 = BruteSolution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(obj1.longestOnes(nums, k))


obj2 = OptimalSolution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(obj2.longestOnes(nums, k))
        