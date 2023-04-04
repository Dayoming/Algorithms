import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
result = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 상, 하, 좌, 우 검색
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append([a, b])
    # 첫번째 집 a, b 방문 처리
    graph[a][b] = 0
    # 첫번째 집 a, b를 방문했기 때문에 1로 시작
    count = 1

    # 큐가 존재하는 동안
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위를 벗어나는 경우
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            
            # 만약 방문하지 않은 집이라면
            if graph[nx][ny] == 1:
                # 방문한 집은 0으로 만든다
                graph[nx][ny] = 0
                queue.append([nx, ny])
                count += 1
    
    return count

# 그래프의 원소가 1일때 bfs로 집 방문
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            result.append(count)

# 오름차순 정렬
result.sort()

# 총 단지수
print(len(result))

# 각 단지내 집의 수
for k in result:
    print(k)