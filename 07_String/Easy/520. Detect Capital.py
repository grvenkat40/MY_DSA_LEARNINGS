class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        elif word.lower() == word:
            return True
        elif word.capitalize() == word:
            return  True
        else:
            return False
obj = Solution()
word = "USA"
print(obj.detectCapitalUse(word))