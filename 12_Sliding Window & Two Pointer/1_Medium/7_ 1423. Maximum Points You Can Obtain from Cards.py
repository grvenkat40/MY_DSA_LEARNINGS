class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        leftsum = 0
        maxSum = 0
        rightsum = 0
        for i in range(k):
            leftsum += cardPoints[i]
        maxSum = leftsum

        rightind = len(cardPoints)-1
        for i in range(k-1, -1, -1):
            leftsum -= cardPoints[i]
            rightsum += cardPoints[rightind]
            rightind -= 1
            maxSum = max(maxSum, leftsum+rightsum)
        return maxSum

obj1 = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(obj1.maxScore(cardPoints, k))