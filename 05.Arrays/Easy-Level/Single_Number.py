def my_better_method(nums):
    hash={}
    for i in nums:                  #Time: O(2N), Space: O(N/2)
        hash[i]=hash.get(i,0)+1
    for value in hash.keys():
        if hash[value]==1:
            print(value)

def optimal_methond(nums):
    unique=0
    for i in nums:                     # Time: O(N) ,Space: O(1)
        unique ^=i
    print(unique)

nums = [4,1,2,1,2]
my_better_method(nums)

optimal_methond(nums)