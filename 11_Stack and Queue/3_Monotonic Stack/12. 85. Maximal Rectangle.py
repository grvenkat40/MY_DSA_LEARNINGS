class Solution:
    def maximalRectangle(self, matrix) -> int:
        n = len(matrix)
        m = len(matrix[0])
        maxArea = 0
        preSumMat = [[0]*m for _ in range(n)]
        for col in range(m):
            sum = 0
            for row in range(n):
                if matrix[row][col] == "1":
                    sum += 1
                else:
                    sum = 0
                preSumMat[row][col] = sum
        for i in range(n):
            maxArea = max(maxArea, self.LargestRectangleHist(preSumMat[i]))
        return maxArea

    def LargestRectangleHist(self, arr):
        stack = []
        maxi = 0
        n = len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                ele = arr[stack.pop()]
                nse = i
                pse = -1 if not stack else stack[-1]
                maxi = max(maxi, (ele*(nse - pse -1))) 
            stack.append(i)
        while stack:
            ele = arr[stack.pop()]
            nse = n
            pse = -1 if not stack else stack[-1]
            maxi = max(maxi, (ele*(nse - pse - 1)))
        return maxi
    
obj = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(obj.maximalRectangle(matrix))