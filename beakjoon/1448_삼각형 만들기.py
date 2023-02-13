# 수학, 그리디 알고리즘, 정렬
import sys
from itertools import combinations

n = int(sys.stdin.readline())
arr = []
answer = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

for i in combinations(arr, 3):
    if i[0] < i[1] + i[2]:
        answer.append(sum(i))

if answer:
    print(max(answer))
else:
    print(-1)