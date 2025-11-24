import math
class PrimeFactor:
    def Prime_factors(self, n):
        result = []
        N = math.sqrt(n)
        for i in range(2, int(N)+1):
            if n % i == 0:
                if self.prime(i) :
                    result.append(i)
                if n//i != i:
                    if self.prime(n//i):
                        result.append(n//i)
        return result
    def prime(self, i):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:
            return True
        else:
            return False
        

    def Optimal(self, n):
        result = []
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                result.append(i)
                while n % i ==0:
                    n = n // i
        if n != 1:
            result.append(n)
        return result
obj = PrimeFactor()
num = 18
print(obj.Prime_factors(num))
num = 18
print(obj.Optimal(num))

print("-----------------------------")

class Solution2:
    def primeFactors(self, queries):
        result = []
        for i in queries:
            ans = []
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    ans.append(j)
                    while i % j == 0:
                        i = i // j
            if i != 1:
                ans.append(i)
            result.append(ans)  
        return result

obj2 = Solution2()
queries = [2, 3, 4, 5, 6]
print(obj2.primeFactors(queries))