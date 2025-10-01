from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result=True
        ran_count=Counter(ransomNote)
        maga_count=Counter(magazine)
        if ran_count-maga_count:
            return False
        else:
            return True
obj=Solution()
ransomNote = "aa"
magazine = "aab"
print(obj.canConstruct(ransomNote,magazine))