class Solution:
    def decimalRepresentation(self, n: int) -> list[int]:
        res = []
        i = 0
        while n>0:
            last = n % 10
            ans = last*(10**i)
            if ans == 0:
                pass
            else:
                res.append(ans)
            i += 1
            n = n//10
        return res[::-1]

obj = Solution()
print(obj.decimalRepresentation(4598))