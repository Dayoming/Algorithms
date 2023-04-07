n = int(input())
gap = 0
m = 1

for i in range(n):
    print(' ' * gap, end='')
    print('*' * (2 * n - m))
    m += 2
    gap += 1
    