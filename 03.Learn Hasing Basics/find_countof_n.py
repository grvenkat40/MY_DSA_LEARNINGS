n=10
arr=[1,2,6,2,1,8,4,6,6,9]
print(arr)
hash={}
# hash_arr=[0]*(n+5)
# print(hash_arr)

"""Precomputing the count of a number"""
for num in arr:
    hash[num]=hash.get(num,0)+1

# for i in range(n):
#     hash_arr[arr[i]]+=1

# print(hash_arr)
# max_ele=max(hash_arr)
# print("Majority Value is :",hash_arr.index(max_ele))
n=int(input("Enter number: "))
print(f'{n}:{hash[n]}')
print(hash)

