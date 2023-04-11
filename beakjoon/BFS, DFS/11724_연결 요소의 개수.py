import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
# 방문을 확인할 리스트
visited = [False for _ in range(n + 1)]
# 연결 요소의 개수
count = 0

# 각 노드가 연결된 정보를 리스트로 표현
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for i in range(1, len(graph)):
    if visited[i] == False:
        bfs(graph, i, visited)
        count += 1

print(count)