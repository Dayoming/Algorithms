n = int(input())
star = 1
gap = (2 * n) - (2 * star)

for _ in range(n):
    print('*' * star, end='')
    print(' ' * gap, end='')
    print('*' * star)
    star += 1
    gap -= 2


star -= 2
gap += 4

for _ in range(n):
    print('*' * star, end='')
    print(' ' * gap, end='')
    print('*' * star)
    star -= 1
    gap += 2