from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        freq = Counter(s)
        for ch in freq:
            if freq[ch] < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        return len(s)

obj = Solution()
print(obj.longestSubstring(s = "ababbc", k = 2))