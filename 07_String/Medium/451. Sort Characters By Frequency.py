def find_freq_rev(s):
    hash={}
    for ch in s:
        hash[ch]=hash.get(ch,0)+1
    print(hash)
    sorted_s=sorted(hash.items(),key=lambda x: (-x[1],x[0])) #-x[1] is decreasing order freq and x[0] asc order by the char
    print(sorted_s)
    result=[ch*f for ch,f in sorted_s if f>0]
    print(''.join(result))



# s = "tree"
s = "Aabb"
find_freq_rev(s)