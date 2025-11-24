
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        
        sign = True
        if dividend > 0 and divisor < 0:
            sign = False
        if dividend < 0 and divisor > 0:
            sign = False
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while n >= d:
            cnt = 0  # power reference
            while n >= d*(2**(cnt+1)):
                cnt += 1
            ans += 2**cnt
            n = n - (d*(2**cnt))
        if ans > 2**31-1 and sign == True:
            return 2**31-1
        if ans > 2**31 and sign == False:
            return 2**31
        if sign == False:
            return ans*-1
        else:
            return ans

obj = Solution()
dividend = 10
divisor = 3
print(obj.divide(dividend, divisor))