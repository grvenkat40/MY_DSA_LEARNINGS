class palindrom_rec:
    def check_pal(self,i,arr,n):
        if i>(n//2):
            return True
        if arr[i]!=arr[n-i-1]:
            return False
        return self.check_pal(i+1,arr,n)
    
obj=palindrom_rec()
# string="A man, a plan, a canal: Panama".upper()
string="madam".upper()
s=list("".join(char for char in string if char.isalpha()))
print(s)
n=len(s)
print(obj.check_pal(0,s,n))