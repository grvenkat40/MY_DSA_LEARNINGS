class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        hash = {}
        for ch in s:
            if ch in vowels:
                hash[ch] = hash.get(ch, 0) + 1
        sortHash = dict(sorted(hash.items(), key=lambda x:-x[1]))
        new = list(s)
        for i, ch in enumerate(new):
            if ch in vowels: 
                firstKey = next(iter(sortHash))
                new[i] = firstKey
                sortHash[firstKey] -= 1
                if sortHash[firstKey] == 0:
                    del sortHash[firstKey]
        return "".join(new)
obj = Solution()
print(obj.sortVowels(s = "leetcode"))