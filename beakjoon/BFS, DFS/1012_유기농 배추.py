import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    # 배추밭 0으로 초기화
    field = [[0 for _ in range(m)] for _ in range(n)]
    # 필요한 배추흰지렁이 마리 수 초기화
    worm = 0

    # 배추밭에 배추 심기
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    
    # 우, 좌, 상, 하 탐색
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    def bfs(field, a, b):
        queue = deque()
        queue.append((a, b))
        # 현재 배추 방문 처리
        field[a][b] = 0

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위에서 벗어나는 경우 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                
                # 만약 상하좌우 중 배추가 심어진 곳이 있다면
                if field[nx][ny] == 1:
                    # 0으로 만들고 큐에 추가한다.
                    field[nx][ny] = 0
                    queue.append((nx, ny))

    # 배추밭을 돌아다니면서 배추가 심어져 있다면 bfs로 탐색
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(field, i, j)
                worm += 1
    
    print(worm)
