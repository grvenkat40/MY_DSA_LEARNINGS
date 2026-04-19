from collections import Counter
class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        res = []
        freq = Counter(nums[:k])
        def compute_sum(freq):
            items = sorted(freq.items() , key=lambda t: (-t[1], -t[0]))
            total = 0
            for i in range(min(x, len(items))):
                val, cnt = items[i]
                total += val * cnt
            return total
        res.append(compute_sum(freq))
        for j in range(k, len(nums)):
            out = nums[j-k]
            freq[out] -= 1
            if freq[out] == 0:
                del freq[out]
            freq[nums[j]] += 1
            res.append(compute_sum(freq))
        return res

obj = Solution()

print(obj.findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))