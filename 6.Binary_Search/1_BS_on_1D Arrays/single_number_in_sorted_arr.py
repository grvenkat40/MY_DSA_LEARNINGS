def findsingle(nums):
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0]!=nums[1]:
        return nums[0]
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]
    i=0
    j=n-2
    while i<=j:
        mid=(i+j)//2
        if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        if (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
            i=mid+1
        else:
            j=mid-1
    return -1

# nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6] 
# nums = [1, 1, 3, 5, 5]
# nums=[1,2,2]
nums=[1,1,4]
print(findsingle(nums))