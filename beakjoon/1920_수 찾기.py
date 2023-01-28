# 수 찾기
# 이진탐색으로 구현
import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    idx = binary_search(find[i], A)

    print(idx)