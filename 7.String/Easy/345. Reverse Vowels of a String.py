class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel="AEIOUaeiou"
        S=list(s)
        i=0
        j=len(S)-1
        while i<=j:
            if S[i] in vowel:
                if S[j] in vowel:
                    S[i],S[j]=S[j],S[i]
                    j-=1
                    i+=1
                else:
                    j-=1
            else:
                i+=1
        return ''.join(S)

obj=Solution()
s = "IceCreAm"
print(obj.reverseVowels(s))
