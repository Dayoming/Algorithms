# 다이얼

seq = input()
time = 0

for i in seq:
    if i in 'ABC':
        time = time + 3
    elif i in 'DEF':
        time = time + 4
    elif i in 'GHI':
        time = time + 5
    elif i in 'JKL':
        time = time + 6
    elif i in 'MNO':
        time = time + 7
    elif i in 'PQRS':
        time = time + 8
    elif i in 'TUV':
        time = time + 9
    elif i in 'WXYZ':
        time = time + 10

print(time)
    
