from collections import defaultdict
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        char_set = [set(word) for word in words]
        max_prod = 0
        for i in range(n):
            for j in range(i+1, n):
                if char_set[i].isdisjoint(char_set[j]):
                    prod = len(words[i]) * len(words[j])
                    max_prod = max(max_prod, prod)
        
        return max_prod 

obj = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(obj.maxProduct(words))