class Solution:
    def addDigits(self, num: int) -> int:
        add=0
        while(num>0):
            last=num%10 # will give the reminder
            add=add+last
            num=num//10 # floor float will terminate the floated points
        return add
obj=Solution()
n=int(input())
print(obj.addDigits(n))