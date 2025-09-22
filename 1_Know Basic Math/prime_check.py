import math
class prime_check():
    def prime(self,n):
        cnt=0
        arr=[]
        sqrt=int(math.sqrt(n))
        for i in range(1,(sqrt+1)): # (i*i==n) (6*6==36)
            if n%i==0:
                arr.append(i)
                cnt+=1
                if n/i != i:
                    arr.append(int(n/i))
                    cnt+=1
        return arr
        return cnt

obj=prime_check()
n=int(input())
prime_count=obj.prime(n)
print(prime_count)
# if prime_count == 2:
    # print(n,"is Prime")

# else:
#     print(n,"is not Prime")