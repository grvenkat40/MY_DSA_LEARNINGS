class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<1 or s=="":
            return ""
        st=0
        e=0
        for i in range(len(s)):
            l1=self.func(s,i,i)
            l2=self.func(s,i,i+1)

            leng=max(l1,l2)
            if leng > (e-st):
                st= i-(leng - 1) //2
                e=i+leng //2
        return s[st:e+1]

    def func(self,s,l,r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            r+=1
            l-=1
        return r-l-1
                    


# s='42'
obj=Solution()
print(obj.longestPalindrome("babad"))
print(obj.longestPalindrome("cbbd"))