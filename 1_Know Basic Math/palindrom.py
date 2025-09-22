class Solution:
    def isPalindrome(self, n):
        self.n=n
        rev=0
        while(n>0):
            last=n%10
            n=n//10
            rev=(rev*10)+last
        print(rev)
        if self.n==rev:
            return True
        else:
            return False

obj=Solution()
n=int(input())
print(obj.isPalindrome(n))