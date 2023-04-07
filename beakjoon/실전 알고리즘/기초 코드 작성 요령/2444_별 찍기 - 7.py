n = int(input())
gap = n - 1

for i in range(1, n + 1):
    print(' ' * gap, end = '')
    print('*' * (2 * i - 1))
    gap -= 1

gap = 0

for j in range(n - 1, 0, -1):
    gap += 1
    print(' ' * gap, end = '')
    print('*' * (2 * j - 1))