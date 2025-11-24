def longest_sub_array_sum(nums,k):
    n=len(nums)
    left=0              #O(n**2)
    right=0
    sum=nums[right]
    max_len=0
    while(right<n):
        while(left<=right and sum>k):
            sum-=nums[left]
            left+=1
        if sum==k:
            max_len=max(max_len,right-left+1)
        
        right+=1
        if right<n:
            sum+=nums[right]
        
    print('n**2 mathod',max_len)

def max_leg_sum(nums,k):
    prefix_sum = 0
    prefix_index = {}                        #O(N)
    max_len = 0
    for i,num in enumerate(nums):
        prefix_sum+=num
        if prefix_sum == k:
            max_len= i+1
        if (prefix_sum-k) in prefix_index:
            max_len = max(max_len,i-prefix_index[prefix_sum-k])
        if prefix_sum not in prefix_index:
            prefix_index[prefix_sum] = i
    return f'O(N) methon {max_len}'

nums = [10, 5, 2, 7, 1, 9]
k=15
longest_sub_array_sum(nums,k)
print(max_leg_sum(nums,k))