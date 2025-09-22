class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        self.Rbubble(nums,n)
        return nums
    def Rbubble(self,nums,n):
        if n==1:
            return
        for i in range(0,n-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
        self.Rbubble(nums,n-1)
        
obj=Solution()
nums=[9,5,1,7,2,4]
print("Before Sort : ",nums)
print("After sort : ",obj.bubbleSort(nums))
# print(nums)