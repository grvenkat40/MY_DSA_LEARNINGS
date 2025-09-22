def Remove_duplicates(arr):
    i=0
    j=1
    while j<len(arr):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
        j+=1
    return i+1
arr=[0,0,3,3,5,6]
print(arr)
print(Remove_duplicates(arr))
print(arr[:4])

