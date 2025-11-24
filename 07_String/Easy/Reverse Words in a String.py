class Solution:
    def reverseWords(self, s: str) -> str:
        space=0
        strs=''
        for i in range(len(s)):
            if s[i] !=" ":
                strs+=s[i]
                space=0
            if s[i] == " ":
                space+=1
                if space>1:
                    pass
                else:
                    strs+=s[i]
        words=strs.split(" ")
        i=0
        j=len(words)-1
        while i<=j:
            words[i],words[j]=words[j],words[i]
            i+=1
            j-=1
        return " ".join(words).strip()
        
obj=Solution()
s = "the sky is blue"
print(obj.reverseWords(s))