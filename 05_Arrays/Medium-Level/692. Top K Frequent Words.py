from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        hash = Counter(words)
        sorted_hash = sorted(hash.items(), key=lambda x:(-x[1], x[0]))
        return [sorted_hash[key][0] for key in range(k)]
    
    def topKFreq(self, words, k):
        n = len(words)
        hash = Counter(words)
        bucket = [[] for _ in range(n+1)]
        for word, cnt in hash.items():
            bucket[cnt].append(word)
        
        res = []
        for freq in range(n, 0, -1):
            if not bucket[freq]:
                continue
            bucket[freq].sort()
            for word in bucket[freq]:
                res.append(word)
                if len(res) == k:
                    return res
        return res

obj = Solution()
print(obj.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
print(obj.topKFreq(words = ["i","love","leetcode","i","love","coding"], k = 2))