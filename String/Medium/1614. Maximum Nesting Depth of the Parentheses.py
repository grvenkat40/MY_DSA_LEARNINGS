def find_max_nestDepth_parantheses(s):
    maxi=0
    cnt=0
    for ch in s:
        if ch == '(':
            cnt+=1
        elif ch == ')':
            maxi=max(cnt,maxi)
            cnt-=1
    return maxi





# s = "(1+(2*3)+((8)/4))+1"   #Digit 8 is inside of 3 nested parentheses in the string
s ="(1)+((2))+(((3)))"      #Digit 3 is inside of 3 nested parentheses in the string.
print(find_max_nestDepth_parantheses(s))