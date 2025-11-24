"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place."""

class Solution:
    #Brute Force Solution
    def Brute_setZeroes(self, matrix, m, n):
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    self.mark_row(row)
                    self.mark_col(col)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == -1:
                    matrix[row][col] = 0
        return f"Brute Solution : {matrix}" 
    
    def mark_row(self, i):
        for c in range(len(matrix)):
            if matrix[i][c] != 0:
                matrix[i][c] = -1
    def mark_col(self,j):
        for r in range(len(matrix)):
            if matrix[r][j] != 0:
                matrix[r][j] = -1 
        
    #Better Solution
    def Better_setZeroes(self, matrix, m , n):
        row = [0]*m
        col = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0
        return f'Better Solution : {matrix}'
    
obj = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
m = len(matrix)
n = len(matrix[0])
print(obj.Brute_setZeroes(matrix, m, n))
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(obj.Better_setZeroes(matrix, m, n))