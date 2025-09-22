import math
class Solution:
    def smallestDivisor(self, nums, threshold) -> int:
        i=1
        j=max(nums)
        # ans=-1
        while i<=j:
            mid=(i+j)//2
            if self.findDivisor(nums,mid,threshold) == True:
                # ans=mid
                j=mid-1
            else:
                i=mid+1
        return i
    def findDivisor(self,nums,mid,threshold):
        sum=0
        for n in nums:
            sum+=(math.ceil(n/mid))
        if sum<=threshold:
            return True
        else:
            return False
        
obj=Solution()
nums = [1,2,5,9]
threshold = 6       #5
# nums = [44,22,33,11,1]
# threshold = 5           #44


print(obj.smallestDivisor(nums, threshold))