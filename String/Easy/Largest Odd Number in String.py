class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)-1
        max_odd=''
        for i in range(n,-1,-1):
            if int(num[i])%2==1:
                max_odd=num[:i+1]
                break
        return max_odd
        
obj=Solution()
num = "52"
# num = "35427"
print(obj.largestOddNumber(num))