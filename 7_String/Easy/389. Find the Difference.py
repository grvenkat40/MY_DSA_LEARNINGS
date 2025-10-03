class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result=0
        for i in range(len(s)):
            result^=ord(s[i])
        for j in range(len(t)):
            result^=ord(t[j])
        return chr(result)
    
obj=Solution()
s = "abcd"
t = "abcde"
# s = ""
# t = "y"
print(obj.findTheDifference(s,t))