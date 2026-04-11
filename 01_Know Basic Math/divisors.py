import math

# class divisors:
#     def divised(self,n):
#         arr=[]
#         for i in range(1,n+1):
#             if n%i==0:
#                 arr.append(i)
#         return arr
# obj=divisors()
# n=int(input())
# print(obj.divised(n))

class divisors:
    def divised(self,n):
        arr=[]
        sqrt=int(math.sqrt(n))
        print(sqrt)
        for i in range(1,sqrt+1):
            if n%i==0:
                print(n,i,"->", n%i)
                arr.append(i)
                if n/i !=i:
                    print(n,i,"->",n/i)
                    arr.append(int(n/i))
        return arr
obj=divisors()
n=int(input())
print(sorted(obj.divised(n)))
