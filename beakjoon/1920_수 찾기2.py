import sys

N = int(sys.stdin.readline())
A = dict()
temp = map(int, sys.stdin.readline().split())

for element in temp:
    if element not in A:
        A[element] = 1

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for element in B:
    if element not in A:
        print(0)
    else:
        print(1)