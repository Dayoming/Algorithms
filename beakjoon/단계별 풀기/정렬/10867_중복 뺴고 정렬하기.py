# 중복 빼고 정렬하기
import sys

n = int(sys.stdin.readline())
arr = list(set(map(int, sys.stdin.readline().split())))
arr.sort()
print(*arr)