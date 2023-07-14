from collections import deque

def bfs(visited, n):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        # 만약 수빈이가 동생을 찾았다면(같은 좌표라면)
        if x == k:
            print(visited[x])
            break
        
        # 걸어서 왼쪽, 오른쪽, 순간이동하는 방법이 있음
        for i in (x - 1, x + 1, x * 2):
            # 좌표를 벗어나지 않아야 함
            if 0 <= i and i <= MAX_NUM:
                # 방문한 좌표가 아직 방문하지 않은 좌표라면 이전 방문까지 걸렸던 초수 + 1초
                if not visited[i]:
                    visited[i] = visited[x] + 1
                    queue.append(i)

# 수빈이가 있는 위치 N과 동생이 있는 위치 K
n, k = map(int, input().split())
# 최대 좌표 수 100,000
MAX_NUM = 100000
visited = [0 for _ in range(MAX_NUM + 1)]

bfs(visited, n)