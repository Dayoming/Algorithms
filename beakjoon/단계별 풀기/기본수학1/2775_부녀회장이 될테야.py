t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    apart = [x for x in range(1, n + 1)]
    for j in range(k):
        for l in range(1, n):
            apart[l] += apart[l - 1]
    print(apart[-1])