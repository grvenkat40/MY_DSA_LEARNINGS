class Solution: 

    #With New matrix
    def rotate_with_new(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        new = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                new[j][n-i-1] = matrix[i][j]
        return new

    #Without New Matrix
    def rorate_inplace(self,matrix):
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix[0])):
            matrix[i].reverse()
        return matrix



obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(obj.rotate_with_new(matrix))
print(obj.rorate_inplace(matrix))