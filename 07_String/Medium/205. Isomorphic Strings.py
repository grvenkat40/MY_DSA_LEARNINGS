def find_isomorphic(s,t):
    S=len(s)
    T=len(t)
    m1, m2 = [0]*256, [0]*256
    for i in range(S):
        if m1[ord(s[i])] != m2[ord(t[i])]:
            return False
        m1[ord(s[i])]=i+1
        m2[ord(t[i])]=i+1
    return True


# s = "egg"
# t = "add"
s = "foo"
t = "bar"
print(find_isomorphic(s,t))