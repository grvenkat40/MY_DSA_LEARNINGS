def findMin(nums):
    i=0
    j=len(nums)-1
    mini=float('inf')
    while i<=j:
        mid=(i+j)//2
        if nums[i] <= nums[mid]:
            mini=min(mini,nums[i])
            i=mid+1
        elif nums[mid] <= nums[j]:
            mini=min(mini,nums[mid])
            j=mid-1
        else:
            min(nums[i],mini)
    return mini

nums=[3,4,5,1,2]
print(findMin(nums))