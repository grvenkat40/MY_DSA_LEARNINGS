def search_rorate_2(nums,target):
    i=0
    j=len(nums)-1
    while i<=j:
        mid=(i+j)//2
        if nums[mid] == target:
            return True
        if nums[i] == nums[mid] and nums[mid] == nums[j]:
            i+=1
            j-=1
        if nums[i] <= nums[mid]:
            if nums[i] <= target and target < nums[mid]:
                j=mid-1
            else:
                j=mid+1
        else:
            if nums[mid] <= target and target <= nums[j]:
                i=mid+1
            else:
                j=mid+1
    return False


# nums = [2,5,6,0,0,1,2]
# target = 0
nums =[1,0,1,1,1,1]
target = 0
print(search_rorate_2(nums,target))