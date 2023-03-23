# 선택 정렬
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(N - 1, 0, -1):
    max_idx = arr.index(max(arr[:i + 1]))
    if max_idx != i:
        arr[max_idx], arr[i] = arr[i], arr[max_idx]
        cnt += 1
    
    if cnt == K:
            print(arr[max_idx], arr[i])
            exit()

print(-1)