class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s and "." in s:
            result = ""
            at = -1
            for i, c in enumerate(s):
                if c == "@":
                    at = i
                    break
            result = s[0] + "*****" + s[at-1] + s[at:]
            return result.lower()
        else:
            separation = {'+', '-', '(', ')', ' '}
            chr_set = [c for c in s if c.isdigit()]
            cnty_code = 0
            result = ""
            if len(chr_set) == 10:
                cnty_code = 0
                result = "***-***-"
            elif len(chr_set) == 11:
                cnty_code = 1
                result = "+*-***-***-"
            elif len(chr_set) == 12:
                cnty_code = 2
                result = "+**-***-***-"
            else:
                cnty_code = 3
                result = "+***-***-***-"
            return  result + "".join(chr_set[-4:])
            
obj = Solution()
s = "86-(10)12345678"
print(obj.maskPII(s))