# Example with O(n**2)

nums=[13,24,46,20,9,52]
print("Before Sorting : ",nums)
for i in range(len(nums)):
    didswap=0
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
            didswap=1
        
        # if didswap==0:
        #     break
        print("times")

print("After Sorting : ",nums)

# Example with O(n)

nums=[1,2,3,4,5]
print("Before Sorting : ",nums)
for i in range(len(nums),1,-1):
    didswap=0
    for j in range(0,i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            didswap=1
        

    if didswap==0:
        print("All set No Swap")
        break
    print("times")

print("After Sorting : ",nums)