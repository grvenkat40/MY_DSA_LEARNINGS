from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque((t, i) for i, t in enumerate(tickets))
        time = 0
        while q:
            ti, ind = q.popleft()
            if ti > 0:
                time += 1
                ti -= 1
                if ind == k and ti == 0:
                    return time
                q.append((ti,ind))

obj =Solution()
tickets = [2,3,2]
k = 2
print(obj.timeRequiredToBuy(tickets, k))