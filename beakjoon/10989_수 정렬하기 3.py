import sys

n = int(sys.stdin.readline())

# 10000개의 배열을 미리 만듬
arr = [0 for i in range(10000)]

for _ in range(n):
    number = int(sys.stdin.readline())
    arr[number - 1] += 1

for i in range(10000):
    if arr[i] > 0:
        for j in range(arr[i]):
            print(i + 1)