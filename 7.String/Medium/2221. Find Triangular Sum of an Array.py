class Solution:
    def triangularSum(self, nums) -> int:
        l=len(nums)

            #https://leetcode.com/problems/find-triangular-sum-of-an-array/description/
            
        # result=[nums]
        # for i in range(l-1):
        #     prev=result[-1]
        #     curr=[]
        #     for j in range(len(prev)-1):
        #         value=(prev[j]+prev[j+1])%10
        #         curr.append(value)
        #     result.append(curr)
        # return result[-1][0]


        result=nums
        while l>1:
            result=[(result[i]+result[i+1])%10 for i in range(l-1)]
            l-=1
        return result[0]
    
obj=Solution()
nums = [1,2,3,4,5]
print(obj.triangularSum(nums))