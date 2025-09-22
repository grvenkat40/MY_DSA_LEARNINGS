# Example with O(n**2)

nums=[13,46,24,52,20,9]
print("Before Sorting : ",nums)
for i in range(len(nums)):
    j=i
    while(j>0 and nums[j-1] > nums[j]):
        nums[j-1],nums[j]=nums[j],nums[j-1]
        j-=1
        print("times")
print("After Sorting : ",nums)



# Example with O(n)

nums=[1,2,3,4,5,6]
print("Before Sorting : ",nums)
for i in range(len(nums)):
    j=i
    while(j>0 and nums[j-1] > nums[j]):
        didswap=0
        nums[j-1],nums[j]=nums[j],nums[j-1]
        didswap=1
        j-=1
        if didswap==0:
            break


print("After Sorting : ",nums)
