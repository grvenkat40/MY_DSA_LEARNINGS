class Solution:
    def merge(self, intervals):
        ls = sorted(intervals, key=lambda x : x[0])
        curr = ls[0]
        res = [curr]
        for start, end in ls[1:]:
            if res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res

obj = Solution()
print(obj.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))