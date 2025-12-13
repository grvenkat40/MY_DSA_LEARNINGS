class BruteSolution:
    def kDistinctChar(self, s, k):
        maxLen = 0
        # hash = {}
        for i in range(len(s)):
            hash = {}
            for j in range(i, len(s)):
                hash[s[j]] = hash.get(s[j], 0)+1
                if len(hash) <= k:
                    maxLen = max(maxLen, j-i+1)
                else:
                    break
        return maxLen

"""--------------------------------------------------------"""
class BetterSolution:
    def kDistinctChar(self, s, k):
        l=r=maxLen = 0
        hash = {}
        while r < len(s):
            hash[s[r]] = hash.get(s[r], 0)+1
            while len(hash) > k:
                hash[s[l]] = hash.get(s[l], 0)-1
                if hash[s[l]] == 0:
                    hash.pop(s[l])
                l += 1
            if len(hash) <= k:
                maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen

obj = BruteSolution()
s = "aababbcaacc"
k = 2
print(obj.kDistinctChar(s, k))


obj1 = BetterSolution()
s = "aababbcaacc"
k = 2
print(obj1.kDistinctChar(s, k))
