class BruteSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        for i in range(len(s)):
            hash = [0]*26
            maxFreq = 0
            for j in range(i, len(s)):
                hash[ord(s[j]) - ord("A")] += 1
                maxFreq = max(hash[ord(s[j]) - ord("A")], maxFreq)
                changes = (j-i+1) - maxFreq
                if changes <= k:
                    maxLen = max(maxLen, j-i+1)
                else:
                    break
        return maxLen

"""----------------------------------------------------------------------"""

class BetterSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        l = 0
        r = 0
        maxFreq = 0
        hash = [0]*26
        while r < len(s):
            hash[ord(s[r]) - ord("A")] += 1
            maxFreq = max(hash[ord(s[r]) - ord("A")], maxFreq)
            while (r-l+1-maxFreq) > k:
                hash[ord(s[l]) - ord("A")] -= 1
                for i in range(25):
                    maxFreq = max(hash[i], maxFreq)
                l += 1
            if (r-l+1-maxFreq) <= k:
                maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen

obj1 = BruteSolution()
s = "AABABBA"
k = 1
print(obj1.characterReplacement(s, k))

obj2 = BetterSolution()
s = "AABABBA"
k = 1
print(obj2.characterReplacement(s, k))