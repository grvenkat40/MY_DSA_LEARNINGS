def Number_of_NGEs_to_the_right(arr, indices):
    i = indices[0]
    j = indices[-1]
    cnt1 =0
    cnt2 = 0
    for n in range(i+1, len(arr)):
        if arr[0] < arr[n]:
            cnt1 +=1 
    for n in range(j+1, len(arr)):
        if arr[j] < arr[n]:
            cnt2 += 1
    return [cnt1, cnt2]

# arr = [3, 4, 2, 7, 5, 8, 10, 6]
# indices = [0, 5]
# arr = [1, 2, 3, 4, 1]
# indices = [0, 3]
arr = [5, 5, 5, 5]
indices = [0, 2]
print(Number_of_NGEs_to_the_right(arr, indices))