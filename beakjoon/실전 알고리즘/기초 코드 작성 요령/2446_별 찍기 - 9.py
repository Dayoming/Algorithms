n = int(input())
star = 2 * n - 1
gap = 0

for _ in range(n):
    print(' ' * gap, end = '')
    print('*' * star)
    gap += 1
    star -= 2

gap -= 2
star += 2

for _ in range(n - 1):
    star += 2
    print(' ' * gap, end = '')
    print('*' * star)
    gap -= 1
