class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_k = 0
        k = 1
        while k*word in sequence:
            max_k = k
            k += 1
        return max_k

obj = Solution()
sequence = "ababac"
word = "ab"
print(obj.maxRepeating(sequence, word))