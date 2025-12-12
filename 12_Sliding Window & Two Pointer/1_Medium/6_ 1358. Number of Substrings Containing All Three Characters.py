class BruteSolution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        a = 'a'
        b = 'b'
        c = 'c'
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if a in sub:
                    if b in sub:
                        if c in sub:
                            result += 1
        return result
    
'''------------------------------------------------'''

class OptimalSolution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        seen = [-1, -1, -1]
        for i in range(len(s)):
            seen[ord(s[i]) - ord('a')] = i
            result += (1 + min(seen))
        return result

obj = BruteSolution()
s = "abcabc"
print(obj.numberOfSubstrings(s))

obj1 = OptimalSolution()
s = "abcabc"
print(obj1.numberOfSubstrings(s))