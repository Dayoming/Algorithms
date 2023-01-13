# N과 M (2)
import sys
from itertools import combinations

# N과 M 입력받기
n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n + 1)]

# itertools의 combinations를 사용해 순서를 고려하지 않고 뽑는 경우(중복 비허용) 경우의 수 구하기
# 조합 구하기
for i in combinations(arr, m):
    print(*i)