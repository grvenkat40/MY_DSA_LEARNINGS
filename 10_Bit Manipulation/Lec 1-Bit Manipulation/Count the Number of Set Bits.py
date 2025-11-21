class Solution:
    def countSetBits(self, n: int) -> int:
        cnt = 0
        while n!=0:
            n = n&n-1
            cnt+=1
        return cnt

obj = Solution()
n = 5
print(obj.countSetBits(n))