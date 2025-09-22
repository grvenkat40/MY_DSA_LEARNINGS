def FreqNums(nums):
    hash={}
    for i in nums:
        hash[i]=hash.get(i,0)+1
    list_itmes=[]
    for key,value in hash.items():
        list_itmes.append([key,value])

    print(list_itmes)

nums=[1,2,4,1,5,2]
FreqNums(nums)
