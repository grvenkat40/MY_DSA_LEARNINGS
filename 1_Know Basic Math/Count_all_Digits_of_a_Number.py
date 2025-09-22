# class Solution:
def countDigit(n):
    counts=0
    while(n>0):
        last=n%10
        counts+=1
        n=n//10
    print(counts)

# obj=()
n=int(input())
# Solution.countDigit(n)
countDigit(n)

