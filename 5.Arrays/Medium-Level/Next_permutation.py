def next_permutation(nums):
    index = -1
    n = len(nums)
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            index = i
            break
    if index == -1:
        nums.reverse()
        return nums
    for i in range(n-1,i>index,-1):
        if nums[index] < nums[i]:
            nums[index],nums[i] = nums[i],nums[index]
            break
    nums[index+1:] = nums[index+1:][::-1]
    return nums 

# nums = [1,2,3]
nums = [3,2,1]
print(next_permutation(nums))