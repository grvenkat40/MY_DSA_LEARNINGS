class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
                if i == len(s):
                    return True
        return True if len(s) == i else False

obj = Solution()
print(obj.isSubsequence( s = "abc", t = "ahbgdc"))