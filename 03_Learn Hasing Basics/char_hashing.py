# n=int(input("Enter number : "))
s=input("Enter string: ")

#Precomputing
hash=[0]*256 # ASCII
for i in range(len(s)):
    hash[ord(s[i])]+=1

know_s=input("Enter char to get count of it :")
print(f'{know_s}:{hash[ord(know_s)]}')