def TwoSum_mine(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):              #Time: O(N**2) space:O(1)
            if nums[i]+nums[j] == target:
                print([i,j])
            
def better_optimal_solution(nums,target):
    hash={}
    for i in range(len(nums)):
        n=nums[i]
        need=target-n                               # Time: O(N log N) space:O(N)
        if need in hash:
            print([hash[need],i])
        hash[nums[i]] = hash.get(nums[i],i)

nums=[3,2,4]
target=6
# nums=[2,7,11,15]
# target=17
TwoSum_mine(nums,target)
print()
better_optimal_solution(nums,target)