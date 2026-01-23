class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        l = 0
        r = 0
        cnt = 0
        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                cnt += 1
                l += 1
            r += 1
        return cnt
        
obj = Solution()
g = [1,2]
s = [1,2,3]
print(obj.findContentChildren(g, s))