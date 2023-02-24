from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
dfs_answer = []
bfs_answer = []

for _ in range(M):
  m1, m2 = map(int, input().split())
  # 노드 연결 하기
  graph[m1][m2] = graph[m2][m1] = 1

# 깊이 우선 탐색
def dfs(graph, V):
    dfs_answer.append(V)
    for i in range(len(graph[V])):
       if graph[V][i] == 1 and (i not in dfs_answer):
          dfs(graph, i)

dfs(graph, V)

# 너비 우선 탐색
def bfs(graph, V):
   bfs_answer.append(V)
   queue = deque()
   queue.append(V)
   
   while queue:
      v = queue.popleft()
      for i in range(len(graph[V])):
         if graph[v][i] == 1 and (i not in bfs_answer):
            queue.append(i)
            bfs_answer.append(i)

bfs(graph, V)

print(*dfs_answer)
print(*bfs_answer)