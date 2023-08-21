x, y = map(str, input().split())

rev_x = int(x[::-1])
rev_y = int(y[::-1])

print(int(str(rev_x + rev_y)[::-1]))

