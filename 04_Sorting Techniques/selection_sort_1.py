nums=[13,46,24,52,20,9]
print("Before Printing : ",nums)
for i in range(0,len(nums)-1):
    mini=i
    for j in range(i,len(nums)):
        if nums[j]<nums[mini]:
            nums[mini],nums[j]=nums[j],nums[mini]

print("After Printing : ",nums)
