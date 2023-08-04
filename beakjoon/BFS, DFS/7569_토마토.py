from collections import deque

# Read input
m, n, h = map(int, input().split())
boxes = []
for _ in range(h):
    boxes.append([list(map(int, input().split())) for _ in range(n)])

# 상, 하, 좌, 우, 위, 아래
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    # 익어있는 토마토를 먼저 큐에 넣는다.
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if boxes[i][j][k] == 1:
                    queue.append((i, j, k, 0))

    days = 0
    
    while queue:
        x, y, z, days = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 범위를 넘어가지 않고, 토마토가 들어있다면 days를 하나 늘리고 큐에 넣어준다.
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and boxes[nx][ny][nz] == 0:
                boxes[nx][ny][nz] = 1
                queue.append((nx, ny, nz, days + 1))

    return days

# 가장 마지막으로 반환하는 days가 최단 경로
min_days = bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            # 익히지 못한 토마토가 존재한다면 -1 출력
            if boxes[i][j][k] == 0:
                print(-1)
                exit()

print(min_days)