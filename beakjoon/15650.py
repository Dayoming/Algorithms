# N과 M (2)
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n + 1)]

for i in combinations(arr, m):
    print(*i)