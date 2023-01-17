# N과 M (6)
import sys

n, m = map(int, sys.stdin.readline().split())
# 오름차순으로 출력하기 위해 입력받은 배열 미리 정렬
arr = sorted(list(map(int, sys.stdin.readline().split())))
answer = []

def dfs(depth, index):
    # 깊이가 m과 같으면 answer 출력
    if depth - 1 == m:
        print(*answer)
        return
    
    # index부터 n까지 반복
    for i in range(index, n):
        # 만약 중복이 아니면
        if arr[i] not in answer:
            # answer에 해당 값을 더한다
            answer.append(arr[i])
            # depth를 1 늘린 값과 현재 i를 1 늘린 값을 재귀호출로 전달
            dfs(depth + 1, i + 1)
            # 재귀호출이 끝나면 answer의 마지막 요소를 삭제
            answer.pop()

dfs(1, 0)
