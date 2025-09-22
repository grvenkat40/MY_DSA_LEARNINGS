"""The upper bound algorithm finds the first and smallest index in a sorted array where 
the value at that index is greater than a given key i.e. x."""
class Solution:
    def upperBound(self, nums, x):
        i=0
        j=len(nums)-1
        ans=-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]>x:
                j=mid-1
                ans=mid
            else:
                i=i=mid+1
        return ans
obj=Solution()
x = 5
nums = [3,5,8,15,19]
print(obj.upperBound(nums,x))