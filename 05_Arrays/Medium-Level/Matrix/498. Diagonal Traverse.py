from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        diag = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diag[i+j].append(mat[i][j])
        res = []
        for k in range(m+n-1):
            if k%2 == 0:
                for e in reversed(diag[k]):
                    res.append(e)
            else:
                for e in diag[k]:
                    res.append(e)
        return res

obj = Solution()

print(obj.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))