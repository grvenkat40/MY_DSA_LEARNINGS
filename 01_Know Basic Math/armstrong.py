# n=1634
def counts(n):
    cnt=0
    while(n>0):
    # digi=n%10
        n=n//10
        cnt+=1
    return cnt
def armstrong(n):
    arm=0
    num=n
    while(num>0):
        digi=num%10
        num=num//10
        arm=arm+digi**counts(n)
    return arm

n=int(input("Enter:"))
arms=armstrong(n)
print(arms)
if n==arms:
    print(n,"==",arms," is a Armstrong")
else:
    print(n,"!=",arms," is Not a Armstrong")