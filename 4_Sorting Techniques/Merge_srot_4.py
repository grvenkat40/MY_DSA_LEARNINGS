def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
        
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i] = temp[i-low]

def Msort(arr,low,high):
    if low==high:
        return 
    mid=(low+high)//2
    Msort(arr,low,mid)
    Msort(arr,mid+1,high)
    merge(arr,low,mid,high)

def MergeSort():
    # arr=[7, 4, 1, 5, 3]
    arr=[3,1,2,4,1,5,2,6,4]
    low=0
    high=len(arr)-1
    print("Before Sort :",arr)
    Msort(arr,low,high)
    print("After sort :",arr)

MergeSort()

