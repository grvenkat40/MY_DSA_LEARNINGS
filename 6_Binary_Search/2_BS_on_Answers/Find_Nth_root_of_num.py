class Solution:
    def NthRoot(self, n, m):
        i=1
        j=n
        while i<=j:
            mid=(i+j)//2
            if n**mid==m:
                return mid
            elif n**mid>m:
                j=mid-1
            elif n**mid<m:
                i=mid+1
        else:
            return -1
obj=Solution()
n=4
m=81

print(obj.NthRoot(n,m))