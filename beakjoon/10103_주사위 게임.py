p1 = 100
p2 = 100

n = int(input())

for i in range(n):
    dice1, dice2 = map(int, input().split())
    if dice1 > dice2:
        p2 = p2 - dice1
    elif dice1 < dice2:
        p1 = p1 - dice2

print(p1)
print(p2)