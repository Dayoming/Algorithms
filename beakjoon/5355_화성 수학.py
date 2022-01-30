t = int(input())

for i in range(t):
    mars = list(input().split())
    result = float(mars[0])
    for j in mars:
        if j == '@':
            result = result * 3
        elif j == '%':
            result = result + 5
        elif j == '#':
            result = result - 7
    print('{:.2f}'.format(result))