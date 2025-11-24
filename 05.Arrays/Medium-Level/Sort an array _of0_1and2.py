def my_method(nums):
    for _ in range(len(nums)):
        for i in range(len(nums)-1):        #Time: O(N**2)
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
    print(nums)

def optimal(nums):
    i=0
    j=0
    k=len(nums)-1
    while j<=k:                             #Time: O(N)
        if nums[j]==0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        elif nums[j]==1:
            j+=1
        else:
            nums[j],nums[k]=nums[k],nums[j]
            k-=1
    print(nums)

nums=[0,2,1,0,1,2,1]
my_method(nums)
print()
optimal(nums)