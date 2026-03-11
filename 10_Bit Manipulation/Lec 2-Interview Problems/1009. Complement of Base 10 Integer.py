class Solution:
    def bitwiseComplement1(self, n: int) -> int:
        res = ''
        for i in bin(n)[2:]:
            if i == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)

    def bitwiseComplement2(self, n: int) -> int:
        if n == 0:
            return 1
        l = n.bit_length()
        mask = (1 << l) - 1 
        return n ^ mask

obj = Solution()

print(obj.bitwiseComplement1(5))
print(obj.bitwiseComplement2(5))