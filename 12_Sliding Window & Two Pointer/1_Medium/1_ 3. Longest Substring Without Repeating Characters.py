class BruteSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        n = len(s)
        for i in range(n-1):
            hash = [0]*256
            for j in range(i, n):
                if hash[ord(s[j])] == 1:
                    break
                l = j - i +1
                maxLen = max(l, maxLen)
                hash[ord(s[j])] = 1
        return maxLen

"""----------------------------------------------------------------"""

class OptimalSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        n = len(s)
        hash = [-1]*256
        l = 0
        r = 0
        while r < n:
            if hash[ord(s[r])] != -1:      #In the hash map
                if hash[ord(s[r])] >= l:
                    l = hash[ord(s[r])] + 1
            le = r-l+1
            maxLen = max(le, maxLen)
            hash[ord(s[r])] = r
            r += 1
        return maxLen
    
obj = BruteSolution()
# s = "abcabcbb"
s= 'bbbbb'
print(obj.lengthOfLongestSubstring(s))

obj1 = OptimalSolution()
s = "abcabcbb"
# s= 'bbbbb'
print(obj1.lengthOfLongestSubstring(s))