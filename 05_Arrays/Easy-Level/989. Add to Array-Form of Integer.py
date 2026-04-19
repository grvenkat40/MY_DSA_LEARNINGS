class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        curr_num = 0
        for n in num:
            curr_num = curr_num * 10 + n
        total = curr_num + k
        if total == 0:
            return [0]
        res = []
        while total > 0:
            res.append(total%10)
            total //= 10
        return res[::-1]

obj = Solution()
print(obj.addToArrayForm([1,2,3,0], 30))