import sys

n = int(sys.stdin.readline())
answer = -1

for i in range(1, n):
    decomposition = list(str(i))
    sum = 0

    for j in decomposition:
        sum += int(j)
    
    if i + sum == n:
        answer = i
        break

if answer == -1:
    print(0)
else:
    print(answer)
