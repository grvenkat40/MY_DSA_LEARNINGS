def My_method(nums):
    cnt=0
    temp=[]
    for i in nums:
        if i==1:                    #Time: O(N) and Space: O(N)
            cnt+=1
        else:
            temp.append(cnt)
            cnt=0
    temp.append(cnt)
    print(max(temp))


def optimise_method(nums):
    cnt=0
    maxi=0
    for i in nums:                  #Time: O(N) and Space: O(1)
        if i==1:
            cnt+=1
            maxi=max(cnt,maxi)
        else:
            cnt=0
    print(maxi)


nums=[1,1,0,1,1,1]
My_method(nums)
optimise_method(nums)
