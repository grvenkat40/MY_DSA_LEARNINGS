"""The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is 
    greater than or equal to a given key i.e. x."""
"""Input : nums= [1,2,2,3], x = 2
Output:1
Explanation:
Index 1 is the smallest index such that arr[1] >= x."""

def lower_bound(nums,x):
    n=len(nums)
    i=0
    j=n-1
    ans=-1
    while i<=j:
        mid=(i+j)//2
        if nums[mid] >= x:
            j=mid-1
            ans=mid
        else:
            i=mid+1
    return ans


nums= [1,2,2,3]
x = 2
print(lower_bound(nums,x))