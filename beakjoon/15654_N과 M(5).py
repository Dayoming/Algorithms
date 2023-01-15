# N과 M(5)
import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = []

result = list(permutations(numbers, m))
result.sort()

for i in result:
    print(*i)