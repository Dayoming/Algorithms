from collections import deque

n = int(input())
ages = deque()
names = deque()

for _ in range(n):
    name, age = input().split()
    ages.append(int(age))
    names.append(name)

names.rotate(-ages.index(min(ages)))

for i in names:
    print(i)