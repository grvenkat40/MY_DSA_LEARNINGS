class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows <= 0:
            return [[]]
        if numRows == 1:
            return [[1]]
        result = [[1]]
        for i in range(numRows-1):
            prev = result[-1]
            curr = [1]
            for j in range(len(prev)-1):
                curr.append(prev[j] + prev[j+1])
            curr.append(1)
            result.append(curr)
        return result

obj = Solution()
numRows = 5
print(obj.generate(numRows))