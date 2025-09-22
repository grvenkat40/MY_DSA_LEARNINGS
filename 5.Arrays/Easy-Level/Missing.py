def Brute_Missing(nums):
    miss=0
    for i in range(len(nums)):                  # Time: O(N**2)  Space: O(1)
        if i not in nums:
            print("Brute Force method:",i)

def Better_missing(nums):
    l=len(nums)
    hash=(l+1)*[0]
    # print(hash)
    for i in range(len(nums)):                  #Time: O(N)  Space: O(N)
        hash[nums[i]]=1
    # print(hash)
    for j in range(len(hash)):
        if hash[j]==0:
            print("Better Methond:",j)

def Optimize_missing(nums):
    N=len(nums)                                 #Time: O(N)  Space: O(1)
    sum=N*(N+1)//2
    sum2=0
    for i in nums:
        sum2+=i
    print("Sum Method:",sum-sum2)   

    result=len(nums)
    for i in range(len(nums)):
        result ^=i^nums[i]
    print("XOR Method:",result)


nums = [1, 3, 6, 4, 2, 5]
Brute_Missing(nums)
Better_missing(nums)
Optimize_missing(nums)