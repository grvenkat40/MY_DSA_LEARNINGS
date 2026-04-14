class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        res = []
        if num < 0:
            num += 2**32
        while num > 0:
            rem = num%16
            if rem < 10:
                res.append(chr(rem+48))
            else:
                res.append(chr(rem+55))
            num //= 16
        res.reverse()
        return "".join(res).lower()
    
obj = Solution()
print(obj.toHex(num = 26))