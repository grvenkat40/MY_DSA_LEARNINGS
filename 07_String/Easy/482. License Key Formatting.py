class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        st = s.replace("-", "").upper()[::-1]
        new = ""
        for i in range(len(st)):
            if i%k == 0:
                new += "-"
            new += st[i]
        new = new[::-1]
        return new[:-1]
obj = Solution()
s = "5F3Z-2e-9-w"
k = 4
print(obj.licenseKeyFormatting(s, k))