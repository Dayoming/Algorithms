n, m = map(int, input().split())
matrix1 = []
matrix2 = []

for i in range(n):
    matrix1.append(list(map(int, input().split())))

for j in range(n):
    matrix2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(matrix1[i][j] + matrix2[i][j], end=' ')
    print()