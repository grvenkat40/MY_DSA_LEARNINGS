"""Input : nums =[3, 4, 4, 7, 8, 10], x= 5
Output: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7."""


class Solution:
    def getFloorAndCeil(self, nums, x):
        i=0
        j=len(nums)-1
        f=-1
        c=-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid] <= x:
                f=nums[mid]
                i=mid+1
            else:
                j=mid-1

        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid] >= x:
                c=nums[mid]
                j=mid-1
            else:
                i=mid+1


        return f,c
            
    

# nums =[3, 4, 4, 7, 8, 10]
# x= 5
nums =[3, 4, 4, 7, 8, 10]
x= 8
obj=Solution()
print(obj.getFloorAndCeil(nums,x))
