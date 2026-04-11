import math
class prime:
    def finding_Factors(self,n):
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
    
    def prime_printer(self, n):
        def check(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True
        cnt = 0
        num = 2
        while cnt < n:
            if check(num):
                print(num, end=' ')
                cnt += 1
            num += 1


obj=prime()
# n=int(input("enter: "))
# prime_count=obj.finding_Factors(1000)
print_n_prime = obj.prime_printer(1000)
# print(prime_count)
# if prime_count == 2:
#     print(n,"is Prime")
# else:
#     print(n,"is not Prime")

