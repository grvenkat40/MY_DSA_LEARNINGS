class Solution():
    sum=0
    def NnumberSum(self,n):
        if n<1:
            return 
        else:
            self.sum+=n
            self.NnumberSum(n-1)
    
    def NormalSum(self,n):
        sum=0
        for i in range(1,n+1):
            sum+=i
        print("Normal N Sum:",sum)


obj=Solution()
obj.NnumberSum(5)
print("Recursion N Sum:",obj.sum)

obj.NormalSum(5)