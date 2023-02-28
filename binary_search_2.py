# 이진 탐색
# 정렬된 배열에서 특정 수의 개수 구하기
import sys
from bisect import bisect_left, bisect_right

N, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left_idx = bisect_left(arr, x)
right_idx = bisect_right(arr, x)

if right_idx - left_idx == 0:
    print(-1)
else:
    print(right_idx - left_idx)