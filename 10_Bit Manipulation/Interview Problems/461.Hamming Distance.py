class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        cnt = 0
        while ans != 0:
            ans = ans & ans-1
            cnt+=1
        return cnt
    
obj = Solution()
start = 10
goal = 7
print(obj.hammingDistance(start, goal))