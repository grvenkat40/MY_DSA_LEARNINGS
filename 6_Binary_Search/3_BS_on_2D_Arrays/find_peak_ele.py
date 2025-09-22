class Solution:
    def findPeakGrid(self, mat):
        n=len(mat)
        m=len(mat[0])
        i=0
        j=m-1
        while i<=j:
            col = (i+j)//2
            row = self.find_col_max(mat,col,n,m)
            left = mat[row][col-1] if col-1>0 else -1
            right = mat[row][col+1] if col+1<m else -1

            if mat[row][col] > left and mat[row][col] > right:
                return row,col
            elif mat[row][col] < left:
                j=col-1
            elif mat[row][col] < right:
                i=col+1


    def find_col_max(self,mat,col,n,m):
        maxi=mat[0][col]
        row_index=0
        for row in range(1,len(mat)):
            if maxi < mat[row][col]:
                maxi=mat[row][col]
                row_index=row
        return row_index

obj=Solution()
mat = [[10,20,15],[21,30,14],[7,16,32]]
print(obj.findPeakGrid(mat))