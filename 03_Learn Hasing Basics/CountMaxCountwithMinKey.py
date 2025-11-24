def MaxValueMinKey(nums):
    hash={}
    for i in nums:
        hash[i]=hash.get(i,0)+1
    max_ele=max(hash,key=lambda m:hash[m])
    print(hash)
    print(max_ele)


MaxValueMinKey([1, 2, 2, 3, 3, 3])
MaxValueMinKey([4, 4, 5, 5, 6])
MaxValueMinKey([2, 4, 3, 2, 5, 4])