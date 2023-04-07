for _ in range(3):
    score = sum(list(map(int, input().split())))
    
    if score == 0:
        print('D')
    elif score == 1:
        print('C')
    elif score == 2:
        print('B')
    elif score == 3:
        print('A')
    else:
        print('E')