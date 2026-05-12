class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        open = 0
        close = 0
        swaps = 0
        for ch in s:
            if ch == "]":
                close += 1
            else:
                open += 1
            if close > open:
                swaps += 1
                open += 1
                close -= 1
        return swaps

obj = Solution()
print(obj.minSwaps(s = "]]][[["))