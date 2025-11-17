class Solution:
    #Brute Force :- Time ~ O(N*3)
    def Brute_subarraySum(self, nums, k) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1]) == k:
                    cnt+=1
        return cnt

    #Better Approach :- Time = O(N*2)
    def Better_subarraySum(self, nums, k) -> int:
        cnt = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum == k:
                    cnt+=1
        return cnt
    
    #Optimal Approach :- TIme = O(N) and space = O(N)
    def Otpimal_subarraySum(self, nums, k):
        hash = {}
        presum = 0
        cnt = 0
        hash[0] = 1
        for i in range(len(nums)):
            presum += nums[i]
            remove = presum - k
            if remove in hash:
                cnt += hash[remove]
            hash[presum] = hash.get(presum,0)+1
        return cnt
    
obj = Solution()
# nums = [1,1,1]
nums = [1,2,3]
k =3
print(obj.Brute_subarraySum(nums, k))
print(obj.Better_subarraySum(nums, k))
print(obj.Otpimal_subarraySum(nums, k))