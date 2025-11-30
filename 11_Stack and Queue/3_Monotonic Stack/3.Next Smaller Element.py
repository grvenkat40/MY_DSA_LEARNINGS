def nextSamllestNumber(nums):
    n = len(nums)
    nse = [8]*n
    stack = []
    for i in range(n-1, -1,-1):
        while stack and stack[-1] > nums[i]:
            stack.pop()
        if stack:
            nse[i] = stack[-1]
        else:
            nse[i] = -1
        stack.append(nums[i])
    return nse

# arr = [4, 8, 5, 2, 25]
# arr = [10, 9, 8, 7]
arr = [1, 2, 3, 4, 5]
print(nextSamllestNumber(arr))