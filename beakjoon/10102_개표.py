v = int(input())
vote = input()
p1 = 0
p2 = 0

for i in vote:
    if i == 'A':
        p1 += 1
    elif i == 'B':
        p2 += 1

if p1 > p2:
    print('A')
elif p1 < p2:
    print('B')
else:
    print('Tie')