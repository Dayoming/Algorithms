# 깊이 우선 탐색, 너비 우선 탐색
import sys
from collections import deque

n = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

graph = [[0] * (n + 1) for _ in range(n + 1)]

answer = []

for _ in range(pair):
    m1, m2 = map(int, sys.stdin.readline().split())
    graph[m1][m2] = graph[m2][m1] = 1

# 너비 우선 탐색
def bfs(graph):
    answer.append(1)
    queue = deque()
    queue.append(1)

    while queue:
        v = queue.popleft()
        for i in range(len(graph[1])):
            if graph[v][i] == 1 and (i not in answer):
                answer.append(i)
                queue.append(i)

bfs(graph)

print(len(answer) - 1)