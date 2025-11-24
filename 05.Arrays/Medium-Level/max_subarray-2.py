def optimal(nums):
    maxi=float('-inf')
    sum=0
    st=-1
    end=-1
    for i in range(len(nums)):
        if sum==0:
            st=i
        sum+=nums[i]
        if maxi<sum:
            maxi=sum
            end=i+1
        if sum<0:
            sum=0
    print(nums[st:end])
    print(maxi)

nums=[5,4,-1,7,8]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
optimal(nums)