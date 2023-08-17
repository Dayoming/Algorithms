cnt = 0
chess = []
for _ in range(8):
    chess.append(list(map(str, input())))

for i in range(8):
    for j in range(8):
        # i가 짝수면 흰색 칸 먼저 시작, j가 짝수인 경우 흰색 칸
        if i % 2 == 0 and j % 2 == 0 and chess[i][j] == 'F':
            cnt += 1
        # i가 홀수면 검정 칸 먼저 시작
        elif i % 2 != 0 and j % 2 != 0 and chess[i][j] == 'F':
            cnt += 1

print(cnt)