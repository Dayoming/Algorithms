name = list()
result = list()

for i in range(5):
    name.append(input())

for i in name:
    if 'FBI' in i:
        result.append(name.index(i) + 1)

if len(result) == 0:
    print('HE GOT AWAY!')
else:
    print(*result, sep=' ') # * -> Unpacking Operator