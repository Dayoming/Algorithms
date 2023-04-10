# M X N 크기의 보드
m, n = map(int, input().split())
board = []
result = []

for _ in range(m):
    board.append(list(input()))

# 시작점 i, j 설정
for i in range(m - 7):
    for j in range(n - 7):
        draw1 = 0
        draw2 = 0
        # 시작점부터 8 X 8 부분 검사
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # 시작 지점을 2로 나눈 나머지가 0일 때와 1일 때를 이용해서 칠할 색상 결정
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min(result))
        