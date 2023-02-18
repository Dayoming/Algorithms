a, b = map(int, input().split())
arr = []
answer = 0

for i in range(1, b + 1):
    for j in range(i):
        arr.append(i)

for i in range(a - 1, b):
    answer += arr[i]

print(answer)