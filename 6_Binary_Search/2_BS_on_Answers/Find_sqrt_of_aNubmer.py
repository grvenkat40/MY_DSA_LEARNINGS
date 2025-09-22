def find_sqrt(n):
    ans=1
    for i in range(1,n):        #Time: O(n)  Linear method
        if i*i<=n:
            ans=i
        else:
            break
    return ans

def find_sqrt_BS(n):
    i=0
    j=n
    ans=1
    while i<=j:
        mid=(i+j)//2        #Time: O(log n)
        if mid*mid>n:
            j=mid-1
        else:
            ans=mid
            i=mid+1
    return ans

print(find_sqrt(25))
print(find_sqrt(4))
print(find_sqrt(27))
print(find_sqrt(36))
print()
print(find_sqrt_BS(25))
print(find_sqrt_BS(4))
print(find_sqrt_BS(27))
print(find_sqrt_BS(39))
