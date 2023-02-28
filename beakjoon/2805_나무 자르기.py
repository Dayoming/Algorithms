# 이분 탐색
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(trees)
answer = 0

while left <= right:
    # 잘린 나무의 합을 저장할 변수
    result = 0
    mid = (left + right) // 2

    for i in trees:
        if i > mid:
            result += i - mid

    # 잘라진 나무의 합이 M보다 작으면 너무 크게 자른 것
    if result < M:
        right = mid - 1 # 더 작게 잘라본다
    else: # 잘라진 나무의 합이 M보다 크거나 같으면 잘 자른 것
        answer = mid # 답에 mid를 저장하고
        left = mid + 1 # 최댓값을 찾아야 하므로 더 크게 잘라본다

print(answer)