def left_rotate(arr,k):
    n=len(arr)
    k%=n
    for _ in range(k):                     #|
        temp=arr[0]                        #| arr[:]=arr[k:]+arr[:k]
        for j in range(1,n):               #| 
            arr[j-1]=arr[j]                #| 
        arr[n-1]=temp


def right_rotate(arr,k):
    n=len(arr)
    k%=n
    for _ in range(k):                     #| 
        temp=arr[n-1]                      #| arr[:]=arr[-k:]+arr[:-k]
        for j in range(n-1,0,-1):          #| 
            arr[j]=arr[j-1]                #| 
        arr[0]=temp
    

arr=[1,2,3,4,5,6]
print("Original Array: ",arr)
k=3
left_rotate(arr,k)
print("Left Rotated Array: ",arr)

right_rotate(arr,k)
print("Right Rotated Array: ",arr)
