# 수학, 그리디 알고리즘, 정렬
import sys
from itertools import combinations

n = int(sys.stdin.readline())
arr = []
answer = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

for i in range(len(arr) - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        answer = arr[i] + arr[i + 1] + arr[i + 2]
        break
    else:
        answer = -1

print(answer)