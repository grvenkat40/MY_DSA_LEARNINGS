def SecondLargest(arr):
    maxi=arr[0]
    S_maxi=0
    for i in range(len(arr)):
        if maxi<arr[i]:
            S_maxi=maxi
            maxi=arr[i]
        elif maxi>arr[i] and arr[i]>S_maxi:
            S_maxi=arr[i]
    print(maxi,S_maxi)

def SecondSmallest(arr):
    mini=arr[0]
    S_mini=0
    for i in range(len(arr)):
        if mini>arr[i]:
            S_mini=mini
            mini=arr[i]
        elif mini<arr[i] and arr[i]<S_mini:
            S_mini=arr[i]
    print(mini,S_mini)

arr=[6,2,8,9,9,1]
print(arr)
SecondLargest(arr)
SecondSmallest(arr)