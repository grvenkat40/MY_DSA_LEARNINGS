def longest_sub_array_sum(nums,k):
    n=len(nums)
    left=0
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
        
    print(max_len)



nums = [10, 5, 2, 7, 1, 9]
k=15
longest_sub_array_sum(nums,k)