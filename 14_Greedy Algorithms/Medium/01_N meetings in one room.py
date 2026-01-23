class Solution:
    def maxMeetings(self, start, end):
        meetings = []
        for i in range(len(end)):
            meetings.append((start[i], end[i], i))
        print(meetings)
        meetings.sort(key = lambda x:x[1])
        # return meetings
        cnt = 1
        last_meeting = meetings[0][1]
        for i in range(1, len(meetings)):
            if meetings[i][0] > last_meeting:
                cnt += 1
                last_meeting = meetings[i][1]
        return cnt

obj = Solution()
Start = [1, 3, 0, 5, 8, 5]
End = [2, 4, 6, 7, 9, 9]
print(obj.maxMeetings(Start, End))