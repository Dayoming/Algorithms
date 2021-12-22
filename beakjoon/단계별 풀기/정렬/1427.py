# 소트인사이드
import sys

n = sys.stdin.readline().strip()
arr = []
for i in n:
    arr.append(i)

arr.sort(reverse=True)

for i in arr:
    print(i, end='')