from collections import Counter

def BruteForce(s):                  # T.C = O(n**3)
    beauty=0                        # S.C = O(n)
    sub=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            subs=''.join(s[i:j+1])
            sub.append(subs)
    print(sub)      
    for i in range(len(sub)):
        freq=Counter(sub[i])
        maxi , mini = max(freq.values()) , min(freq.values())
        beauty+=(maxi-mini)
    return beauty

def Optimal(s):
    beauty=0
    for i in range(len(s)):
        c=Counter()
        for j in range(i,len(s)):
            c[s[j]]+=1
            print(c)
            maxi=max(c.values())
            mini=min(c.values())
            beauty+=(maxi-mini)
    return beauty


  #5
print("Brute Force Approch: \n")
print(BruteForce('aabcb'))

print("Optimal Approch: \n")
print(Optimal('aabcb'))