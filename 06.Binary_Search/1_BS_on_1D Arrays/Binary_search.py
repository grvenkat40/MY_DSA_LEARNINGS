def search(nums,target):
    n=len(nums)
    i=0
    j=n-1
    while i<=j:
        mid=(i+j)//2
        if target > nums[mid]:
            i=mid+1
        elif target < nums[mid]:
            j=mid-1
        else:
            return mid
    return -1


def Recursive_search(nums,target,i,j):
    if i>j:
        return -1
    mid=(i+j)//2
    if target > nums[mid]:
        i=mid+1
    elif target < nums[mid]:
        j=nums[mid]
    else:
        return mid
    return Recursive_search(nums,target,i,j)

nums = [-1,0,3,5,9,12]
target = 3
print("Normal Binary Search")
print(search(nums,target))

i=0
j=len(nums)-1
print("Recursive Binary Search")
print(Recursive_search(nums,target,i,j))

