"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence."""

class Solution:
    #Brute Force Solution
    def Brute_longestConsecutive(self, nums) -> int:
        longest = 0
        for  i in range(len(nums)):
            n = nums[i]
            cnt=0
            while(self.search(nums, n) == True):
                n = n+1
                cnt+=1
            longest = max(cnt,longest)
        return f'Brute Force : {longest}'
    def search(self,arr,n):
        for i in range(len(arr)):
            if arr[i] == n:
                return True
        return False
    
    #Better Solution
    def Better_longestConsecutive(self, nums) -> int:
        nums.sort()
        longest = 0
        cnt = 0
        last_smaller = float('-inf')
        for i in range(len(nums)):
            if nums[i]-1 == last_smaller:
                cnt+=1
                last_smaller = nums[i]
            elif nums[i] == last_smaller:
                continue
            elif nums[i] != last_smaller:
                cnt = 1
                last_smaller = nums[i]
            longest = max(longest,cnt)
        return f'Better Solution : {longest}'

    #Optimal Solution
    def Optimal_longestConsecutive(self, nums):
        arr = set(nums)
        longest = 0
        cnt = 0
        for i in range(len(arr)):
            if nums[i]-1 in arr:
                continue
            elif nums[i]-1 not in arr:
                cnt = 1
                n = nums[i]
                while n+1 in arr:
                    cnt+=1
                    n = n+1
            longest = max(longest, cnt)
        return f'Better Solution : {longest}'

obj = Solution()
# nums = [100,4,200,1,3,2]
nums = [1,0,1,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
print(obj.Brute_longestConsecutive(nums))
print(obj.Better_longestConsecutive(nums))
print(obj.Optimal_longestConsecutive(nums))