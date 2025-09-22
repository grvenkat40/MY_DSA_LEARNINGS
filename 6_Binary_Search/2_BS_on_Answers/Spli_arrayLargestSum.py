class Split_arr():
    def Split_arr_largeSum(self,nums,k):
        i=max(nums)
        j=sum(nums)
        ans=0
        while i<=j:
            mid=(i+j)//2
            sub_arr= self.find_sub_arr(nums,mid)
            if sub_arr<=k:
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
    def find_sub_arr(self,nums,mid):
        arr=1
        sum=0
        for num in nums:
            if sum+num<=mid:
                sum+=num
            else:
                arr+=1
                sum=num
        return arr

# nums = [7,2,5,10,8]     #18
# k = 2
nums = [1,2,3,4,5]
k = 2   #9
obj=Split_arr()
print(obj.Split_arr_largeSum(nums,k))