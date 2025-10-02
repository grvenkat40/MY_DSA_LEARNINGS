def rotate(s,goal):
    n,m=len(s),len(goal)
    if n != m:
        return False
    for i,c in enumerate(s):
        if c == goal[0]:
            modified=s[i:]+s[:i]
            if modified == goal:
                return True
            else:
                return False
    return False

# s = "abcde"
# goal = "cdeab"
s = "abcde"
goal = "abced"
print(rotate(s,goal))