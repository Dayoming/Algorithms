# 자료 구조, 큐
import sys

arr = []
n = int(sys.stdin.readline())

while True:
    buffer = int(sys.stdin.readline())
    if buffer == -1:
        if len(arr) == 0:
            print('empty')
            break
        else:
            print(*arr)
            break
    elif buffer == 0:
        del arr[0]
    else:
        if len(arr) >= n:
            continue
        else:
            arr.append(buffer)
    