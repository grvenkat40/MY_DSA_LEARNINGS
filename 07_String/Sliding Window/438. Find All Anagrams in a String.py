from collections import Counter
class Solution:
    def MySOlution_findAnagrams(self, s: str, p: str) -> list[int]:
        i = 0
        j = len(p)-1
        res = []
        while j < len(s):
            window = s[i:j+1]
            cnt = 0
            for c in p:
                if p.count(c) == window.count(c):
                    cnt += 1
                else:
                    break
            if cnt == len(p):
                res.append(i)
            i += 1
            j += 1
        return res

    def Optimal_findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        p_cnt = Counter(p)
        window = Counter()
        k = len(p)
        for i in range(len(s)):
            window[s[i]] += 1
            if i >= k:
                if window[s[i-k]] == 1:
                    del window[s[i-k]]
                else:
                    window[s[i-k]] -= 1
            if window == p_cnt:
                res.append(i-k+1)
        return res

obj = Solution()
print(obj.MySOlution_findAnagrams(s = "cbaebabacd", p = "abc"))
print(obj.Optimal_findAnagrams(s = "cbaebabacd", p = "abc"))