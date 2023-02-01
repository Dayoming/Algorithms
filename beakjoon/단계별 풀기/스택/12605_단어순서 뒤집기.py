# 단어순서 뒤집기
import sys

n = int(sys.stdin.readline())
answer = []

for i in range(n):
    arr = list(sys.stdin.readline().rstrip().split())
    arr = arr[::-1]
    answer.append(arr)

case = 1

for j in answer:
    print("Case #%d:" % case, *j)
    case += 1