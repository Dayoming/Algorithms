n = int(input())
result = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0, 'AXIS': 0}

for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        result['AXIS'] += 1
    elif x > 0 and y > 0:
        result['Q1'] += 1
    elif x < 0 and y > 0:
        result['Q2'] += 1
    elif x < 0 and y < 0:
        result['Q3'] += 1
    elif x > 0 and y < 0:
        result['Q4'] += 1

for j in result:
    print('{}: {}'.format(j, result[j]))