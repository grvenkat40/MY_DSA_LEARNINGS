# For Number
def largestNumber(nums):
    maxi=nums[0]
    for i in range(1,len(nums)):
        if maxi < nums[i]:
            maxi=nums[i]
    print(maxi)
    
#For Alphabets
def largestAlpha(arr):
    maxi=ord(arr[0])
    for i in range(1,len(arr)):
        if maxi < ord(arr[i]):
            maxi=ord(arr[i])
    print(chr(maxi))

nums= [902, 3, 0, 99, -40]
print(nums)
largestNumber(nums)

arr=['A','U','E','C','H','J','W']
print(arr)
largestAlpha(arr)