def Brute_rearrange_ele(nums):
    posi = []
    negi = []
    result = [0]*len(nums)            # TC-O(N*N/2) and SC- O(N)
    for n in nums:
        if n>0:
            posi.append(n)
        else:
            negi.append(n)
    for i in range(len(nums)//2):
        result[i*2] = posi[i]
        result[i*2+1] = negi[i]
    return f'BruteFOrce Method {result}'

def Optimal_rearrange_ele(nums):
    pos = 0                            # TC-O(N) and SC- O(N)
    negi = 1                
    result = [0]*len(nums)
    for i in range(len(nums)):
        if nums[i]>0:
            result[pos] = nums[i]
            pos+=2
        else:
            result[negi] = nums[i]
            negi+=2
    return f'Optimal Method {result}'


nums = [3,1,-2,-5,2,-4]
print(Brute_rearrange_ele(nums))
nums = [3,1,-2,-5,2,-4]
print(Optimal_rearrange_ele(nums))