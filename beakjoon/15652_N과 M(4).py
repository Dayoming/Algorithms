# N과 M (4)
import sys

n, m = map(int, sys.stdin.readline().split())
answer = []

# 백트래킹 - DFS을 이용해 해결
def dfs(depth, index):
    # 깊이가 m과 같다면 answer 출력
    if depth - 1 == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(index, n + 1):
        # answer에 i 추가
        answer.append(i)
        # 깊이를 1 증가시키고 재귀호출
        dfs(depth + 1, i)
        # 재귀호출이 종료되면 리스트의 마지막 값 삭제
        answer.pop()

dfs(1, 1)
