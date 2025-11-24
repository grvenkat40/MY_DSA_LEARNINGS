def my_method(nums):
    maxi=0
    for i in range(len(nums)):
        sum=0                               #TIme: O(N**2)
        for j in range(i,len(nums)):
            sum+=nums[j]
        maxi=max(sum,maxi)
    print(maxi)

def optimal(nums):
    maxi=float('-inf')
    sum=0
    for i in range(len(nums)):          #Time: O(N)
        sum+=nums[i]
        if maxi < sum:
            maxi=sum
        if sum<0:
            sum=0
    print(maxi)
# nums=[5,4,-1,7,8]
nums = [-2,1,-3,4,-1,2,1,-5,4]
my_method(nums)
print()
optimal(nums)