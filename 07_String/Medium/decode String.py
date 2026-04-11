def decode_String(s):
    res = ""
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        n = 0
        while i<len(s) and s[i].isdigit():
            n = n*10 + int(s[i])
            i += 1
        res += ch * n
    return res

print(decode_String("a12"))