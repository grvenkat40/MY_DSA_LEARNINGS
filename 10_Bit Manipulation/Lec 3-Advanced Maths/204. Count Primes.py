class Solution:
    def Brute_countPrimes(self, n) -> int:
        P_cnt = 0
        for i in range(2, n):
            if self.P_check(i):
                P_cnt += 1
        return P_cnt 

    def P_check(self, n):
        cnt = 0
        for i in range(1,n+1):
            if n%i == 0:
                cnt += 1
        if cnt == 2:
            return True
        else:
            return False
        
    def Optimal_countPrimes(self, n):
        prime = [1] * (n)
        prime[0] = prime[1] = 0
        p = 2
        while p*p <= n:
            if prime[p] == 1:
                for i in range(p*p, n, p):
                    prime[i] = 0
            p+=1
        return sum(prime)
        
obj = Solution()
n = 10
print(obj.Brute_countPrimes(n))
print(obj.Optimal_countPrimes(n))