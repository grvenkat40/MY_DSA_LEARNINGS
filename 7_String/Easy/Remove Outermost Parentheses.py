class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=''
        cnt=0
        for i in range(len(s)):
            if s[i] == ')':
                cnt-=1
            if cnt != 0:
                result+=s[i]
            if s[i] == '(':
                cnt+=1
        return result
    
obj=Solution()
# s = "(()())(())"
s="(()())(())(()(()))"
print(obj.removeOuterParentheses(s))