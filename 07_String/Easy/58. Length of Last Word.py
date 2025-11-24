class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        S=''
        space=0
        for i in range(len(s)):
            if s[i] != " ":
                S+=s[i]
                space=0
            if s[i] == " ":
                space+=1
                if space>1:
                    pass
                else:
                    S+=s[i]
        S=S.split(" ")
        return len(S[-1])
obj=Solution()
s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
print(obj.lengthOfLastWord(s))