class Solution:      
    def findRangeXOR(self, l, r):
        result = 0
        for i in range(l,r+1):
            result ^= i
        return result

obj = Solution()
l = 3
r = 5
print(obj.findRangeXOR(l, r))