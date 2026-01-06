class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        newStr = (s+s)[1:-1]
        print(newStr)
        return s in newStr
obj = Solution()
s = "aba"
print(obj.repeatedSubstringPattern(s))