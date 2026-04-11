class Solution:
    def GCD(self, a, b):
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
        while a>0 and b>0:
            if a>b:
                a=a%b
                print("a",a)
            else:
                b=b%a
                print("b",b)
        if a==0:
            return b
        else:
            return a
            
n1=int(input())
n2=int(input())
obj=Solution()
# print(max(obj.GCD(n1,n2)))
print(obj.GCD(n1,n2))
