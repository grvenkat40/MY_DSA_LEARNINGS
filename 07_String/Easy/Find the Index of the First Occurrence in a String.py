class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)
        if n<m:
            return -1
        for i in range(n-m+1):
            if haystack[i] == needle[0]:
                cnt=1
                for j in range(1,m):
                    if haystack[i+j] == needle[j]:
                        cnt+=1
                    else:
                        break
                if cnt==m:
                    return i  
        return -1    
obj=Solution()
haystack = "sadbutsad"
needle = "sad"
print(obj.strStr(haystack,needle))