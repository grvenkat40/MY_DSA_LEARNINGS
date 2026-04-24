n = int(input())

mat = [[0]*2 for _ in range(n)]

for i in range(n):
    n1, n2 = input().split()
    mat[i][0] = n1
    mat[i][1] = n2

for i in range(len(mat)):
    mini = i
    for j in range(i, len(mat)):
        if mat[j] < mat[mini]:
            mat[mini], mat[j] = mat[j], mat[mini]
print(mat)