def reverseNumber(n):
    rev=0
    while(n>0):
        last=n%10
        n=n//10
        rev=(rev*10)+last
        # print(int(last),end='')
    print(rev)

n=int(input())
reverseNumber(n)
# x=244
# x,last=divmod(x,10)
# print(last)