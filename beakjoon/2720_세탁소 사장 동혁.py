import sys

t = int(sys.stdin.readline())

for _ in range(t):
    c = int(sys.stdin.readline())

    coins = [25, 10, 5, 1]
    count = [0, 0, 0, 0]
    i = 0
    
    while c != 0:
        if c >= coins[i]:
            c -= coins[i]
            count[i] += 1
        else:
            i += 1
    
    print(*count)