class Solution:
    def insertion(self, nums,n):
        if n==0:
            return 
        for i in range(0,n-1):
            j=i
            if(j>0 and nums[j-1]>nums[j]):
                nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1
        self.insertion(nums,n-1)
        # return nums
        
obj=Solution()
nums=[9,5,1,0,2,4]
print("Before Sort : ",nums)
n=len(nums)
obj.insertion(nums,n)
print("After Sort : ",nums)