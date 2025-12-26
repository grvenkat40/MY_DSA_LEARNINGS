from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hash = Counter(s)
        seen = set()
        stack = []
        for ch in s:
            hash[ch] -= 1
            if ch in seen:
                continue
            while stack and ord(ch) < ord(stack[-1]) and hash[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)

obj = Solution()
s = "bcabc"
print(obj.removeDuplicateLetters(s))