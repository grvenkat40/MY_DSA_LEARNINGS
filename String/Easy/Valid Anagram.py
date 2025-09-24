class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        u=set(s)
        for i in u:
            if s.count(i) != t.count(i):
                return False
        return True

obj=Solution()
# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"
print(obj.isAnagram(s,t))