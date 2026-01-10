class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        presum = [0]*(n+1)
        presum[0] = 0
        for i in range(1, n+1):
            presum[i] = presum[i-1] + gain[i-1]
        return max(presum)

obj = Solution()
gain = [-5,1,5,0,-7]
print(obj.largestAltitude(gain))