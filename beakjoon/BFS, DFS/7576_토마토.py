from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
tomatos = []
for _ in range(n):
    tomatos.append(list(map(int, stdin.readline().split())))

queue = deque()

# 익어있는 토마토를 먼저 큐에 넣는다
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            queue.append((i, j))

# 상, 하, 좌, 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 넘어가거나 토마토가 들어있지 않은 칸의 경우 넘어간다
            if nx < 0 or nx >= n or ny < 0 or ny >= m or tomatos[nx][ny] == -1:
                continue
            
            # 익어있지 않은 토마토라면
            if tomatos[nx][ny] == 0:
                # 현재 좌표의 토마토 값을 큐에서 꺼냈던 좌표의 토마토 값 + 1로 바꿔준다. (이전 토마토보다 하루 더 늦게 익었다는 의미) 
                tomatos[nx][ny] = tomatos[x][y] + 1
                # 현재 좌표를 큐에 넣어준다.
                queue.append((nx, ny))

bfs()

days = 0

for i in tomatos:
    for j in i:
        # 익히지 못한 토마토가 존재한다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # tomatos에서 가장 큰 값이 토마토가 모두 익는 최단 경로가 된다
    days = max(days, max(i))

# 첫 날은 제외해준다
print(days - 1)

