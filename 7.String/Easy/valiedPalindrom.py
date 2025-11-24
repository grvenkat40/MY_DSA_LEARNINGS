class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=list("".join(char for char in s if char.isalnum()).lower())
        n=len(clean)
        return self.helper(clean,n)
        # i=0
    def helper(self,clean,n):
        if not clean or len(clean)==1:
            return True
        i=0
        while i<(n//2):
            if clean[i] != clean[n-i-1]:
                return False
            i+=1
        return True
             
obj=Solution()
# s = "A man, a plan, a canal: Panama"
s = "race a car"
print(obj.isPalindrome(s))