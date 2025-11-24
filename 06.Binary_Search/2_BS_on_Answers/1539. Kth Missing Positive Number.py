def kth_missing(arr,k):
    for num in range(len(arr)):
        if arr[num]<=k:
            k+=1
        else:
            break
    return k

def kth_Missing_BS(arr,k):
    i=0
    j=len(arr)-1
    while i<=j:
        mid=(i+j)//2
        missing=arr[mid]-(mid+1)
        if missing<k:
            i=mid+1
        else:
            j=mid-1
    return i+k


# arr=[2,3,4,7,11]
# k=5
arr=[1,2,3,4]
k=2
print(kth_missing(arr,k))
print()
print(kth_Missing_BS(arr,k))