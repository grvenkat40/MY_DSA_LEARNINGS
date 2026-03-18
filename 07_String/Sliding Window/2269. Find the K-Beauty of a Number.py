class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n = str(num)
        i = 0
        j = 0
        cnt = 0
        while j < len(n):
            if (j-i+1) < k:
                j += 1
            elif (j-i+1) == k:
                number = int(n[i:j+1])
                if number != 0 and  num % number == 0:
                    cnt += 1
                i += 1
                j += 1
        return cnt

obj = Solution()
print(obj.divisorSubstrings(num = 430043, k = 2))