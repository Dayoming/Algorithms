answer = 0
minimum = 100

for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        answer += n
        if n < minimum:
            minimum = n

if answer == 0:
    print(-1)
    exit()
else:
    print(answer)
    print(minimum)