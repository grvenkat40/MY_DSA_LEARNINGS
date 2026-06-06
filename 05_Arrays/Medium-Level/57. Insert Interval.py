class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        res = []
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


        # intervals.append(newInterval)
        # intervals.sort(key=lambda x:x[0])
        # merged = [intervals[0]]
        # for start, end in intervals[1:]:
        #     if merged[-1][1] >= start:
        #         merged[-1][1] = max(merged[-1][1], end)
        #     else:
        #         merged.append([start, end])
        # return merged
    
obj = Solution()
print(obj.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))