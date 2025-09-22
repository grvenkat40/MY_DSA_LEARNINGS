def findMin(nums):
    i=0
    j=len(nums)-1
    mini=float('inf')
    while i<=j:
        mid=(i+j)//2
        if nums[i] <= nums[mid]:
            if nums[i]<mini:
                mini=nums[i]
                index=i
            i=mid+1
        elif nums[mid] <= nums[j]:
            if nums[i]<mini:
                mini=nums[i]
                index=i
            j=mid-1
        else:
            min(nums[i],mini)
    return mini,index

nums=[4, 5, 6, 7, 0, 1, 2, 3]
# nums = [4, 5, 1, 2]
# nums=[3, 4, 5, 1, 2]
print(findMin(nums))