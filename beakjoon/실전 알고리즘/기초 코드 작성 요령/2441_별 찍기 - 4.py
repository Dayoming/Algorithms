n = int(input())
gap = 0
star = n

for i in range(n):
    print(' ' * gap, end='')
    gap += 1
    print('*' * star)
    star -= 1