x = int(input())
n = int(input())
cost = 0
answer = 'No'
for i in range(n):
    a, b = map(int, input().split())
    cost += a * b

if cost == x:
    answer = 'Yes'

print(answer)
