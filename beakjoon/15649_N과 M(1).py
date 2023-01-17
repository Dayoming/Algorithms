# N과 M (1)
import sys
from itertools import permutations

# N과 M 입력받기
n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n + 1)]

# itertools의 permutations를 사용해 순서를 고려하여 뽑는 경우(중복 허용) 경우의 수 구하기
for i in permutations(arr, m):
    print(*i)