class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        res = []
        for ch in s:
            if ch == "(":
                open += 1
                res.append(ch)
            elif ch == ")":
                if open > 0:
                    open -= 1
                    res.append(ch)
            else:
                res.append(ch)
        final = []
        for ch in reversed(res):
            if ch == "(" and open > 0:
                open -= 1
                continue
            final.append(ch)
        return "".join(reversed(final))

obj = Solution()
print(obj.minRemoveToMakeValid(s = "lee(t(c)o)de)"))