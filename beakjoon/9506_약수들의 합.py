t = int(input())

while t != -1:
    divisor = list()
    temp = 0
    for i in range(1, t):
        if t % i == 0:
            divisor.append(i)
            temp = temp + i
    if temp != t:
        print(t, 'is NOT perfect.')
    else:
        print(t, ' = ', ' + '.join(str(i) for i in divisor), sep='')
    t = int(input())