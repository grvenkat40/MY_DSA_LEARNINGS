class Solution:
    def myAtoi(self, s) -> int:
        result=0
        i=0
        n = len(s)
        
        while i < len(s) and s[i] == ' ':
            i+=1

        sign=1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            else:
                sign = 1
            i+=1 
        
        while i < n and s[i].isdigit():
            digit = int(s[i])

            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31

            result =(result * 10) + digit
            i+=1
        return result*sign

obj = Solution()
s = " -042"         #-42
# s = "0-1"           #0
# s = "words and 987" #0
print(obj.myAtoi(s))