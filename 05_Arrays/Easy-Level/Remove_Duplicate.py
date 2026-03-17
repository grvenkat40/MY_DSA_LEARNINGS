def Remove_duplicates(arr):
    i=0
    j=1
    while j<len(arr):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
        j+=1
    return i+1
arr=[0,0,3,3,5,6]
print(arr)
ind = Remove_duplicates(arr)
print(arr[:ind])
# -----------------------------------------------
nums = [1,1,2]
i = 0
j = 1
while j < len(nums):
    if nums[i] == nums[j]:
        j += 1
    elif nums[i] != nums[j]:
        nums[i+1] = nums[j]
        i += 1
        j += 1
print(nums[:i+1])