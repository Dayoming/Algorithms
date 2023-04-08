import sys

a, b = map(int, sys.stdin.readline().split())

if a > b:
    count = (a - b) - 1
    print(count)
    for i in range(1, a - b):
        print(b + i, end = ' ')
elif a < b:
    count = (b - a) - 1
    print(count)
    for i in range(1, b - a):
        print(a + i, end = ' ')
else:
    print(0)
    exit()

