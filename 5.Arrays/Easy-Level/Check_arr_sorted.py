def check(arr):
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            pass
        else:
            return False
    return True

arr=[1,2,8,4,5]
print(check(arr))