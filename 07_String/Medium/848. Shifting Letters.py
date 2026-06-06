class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        s = list(s)
        total = 0
        for i in range(len(s)-1, -1, -1):
            total = (total + shifts[i]) % 26
            s[i] = chr(
                (ord(s[i]) - ord("a") + total) % 26 + ord("a")    
            )
        return "".join(s)

obj = Solution()
print(obj.shiftingLetters(s = "abc", shifts = [3,5,9]))