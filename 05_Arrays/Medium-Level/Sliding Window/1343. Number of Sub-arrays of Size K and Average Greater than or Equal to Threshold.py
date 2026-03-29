class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        cnt = 0
        window = sum(arr[:k])
        if (window // k) >= threshold:
            cnt += 1
        for i in range(k, len(arr)):
            window += arr[i]
            window -= arr[i-k]
            if (window // k) >= threshold:
                cnt += 1
        return cnt

obj = Solution()

print(obj.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))