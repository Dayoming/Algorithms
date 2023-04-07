n = int(input())
star = 0
gap = n

for i in range(1, n + 1):
    star = 2 * i - 1
    gap -= 1
    print(' ' * gap, end='')
    print('*' * star)