# Rectangle horizon and vertical input
horizon, vertical = map(int, input().strip().split(' '))
for v in range(0, vertical):  # repeat as vertical
    for h in range(0, horizon):  # repeat as horizon
        print('*', end='')  # Output as many horizontal iterations
    print()  # new line
