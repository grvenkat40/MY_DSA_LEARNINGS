def find_Roman_num(s):
    l=len(s)-1
    result=0
    hash={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    while l>=0:
        if l==0:
            result+=hash[s[l]]
            l-=1
        elif hash[s[l]] > hash[s[l-1]]:
            result+=(hash[s[l]]-hash[s[l-1]])
            l-=2
        else:
            result+=hash[s[l]]
            l-=1
    return result


# s = "III" #III = 3.

# s = "LVIII"   # L = 50, V= 5, III = 3.

s = "MCMXCIV"   # M = 1000, CM = 900, XC = 90 and IV = 4.
print(find_Roman_num(s))