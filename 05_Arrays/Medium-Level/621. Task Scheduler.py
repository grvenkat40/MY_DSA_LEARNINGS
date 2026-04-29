from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        hash = Counter(tasks)
        max_freq = max(hash.values())
        max_cnt =  list(hash.values()).count(max_freq)

        return max(len(tasks), (max_freq-1) * (n+1) + max_cnt )

obj = Solution()
print(obj.leastInterval( tasks = ["A","A","A","B","B","B"], n = 2))