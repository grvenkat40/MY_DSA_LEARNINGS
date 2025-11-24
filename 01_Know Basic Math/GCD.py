class Solution:
    def GCD(self, n1, n2):
        # div=[]
        # if n1>n2:
        #     for i in range(1,n1+1):
        #         if n1%i==0 and n2%i==0:
        #             div.append(i)
        #             if n1/i!=i and n2/i!=i:
        #                 if n1/i==n2/i:
        #                     div.append[n1/i]
        #     return div
        # else:
        #     # div=[]
        #     for i in range(1,n1+1):
        #         if n1%i==0 and n2%i==0:
        #             div.append(i)
        #             if n1/i!=i and n2/i!=i:
        #                 if n1/i==n2/i:
        #                     div.append[n1/i]
        #     return div
        while n1>0 and n2>0:
            if n1>n2:
                n1=n1%n2
            else:
                n2=n2%n1
            if n1==0:
                return n2
            return n1
n1=int(input())
n2=int(input())
obj=Solution()
# print(max(obj.GCD(n1,n2)))
print(obj.GCD(n1,n2))
