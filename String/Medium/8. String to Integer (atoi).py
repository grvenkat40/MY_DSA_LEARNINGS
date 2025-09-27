class Solution:
    def myAtoi(self, s: str) -> int:
        result=0
        i=0
        sign=1
        if s=='':
            return 0
        #Ignoring Leading Spaces
        while i<len(s) and s[i]==' ':
            i+=1
        # Determine the sign 
        if s[i] == '-':
            sign=-1
            i+=1
        if s[i] == '+':
            sign=1
            i+=1
        #Take the Valid numbers
        while i<len(s) and s[i].isdigit():
            result=(result*10) + int(s[i])

            if sign * result > 2**31-1:
                return 2**31-1
            elif sign * result < -2**31:
                return -2**31
            i+=1
        return sign*result
    

obj=Solution()
print(obj.myAtoi('42'))
print(obj.myAtoi("1337c0d3"))
print(obj.myAtoi(" -042"))
print(obj.myAtoi("words and 987"))
print(obj.myAtoi("0-1"))
        
        