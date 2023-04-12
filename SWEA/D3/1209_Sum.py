for test_case in range(10):
    number = int(input())
    arr = []
    
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    
    max_row = 0
    max_col = 0
    max_diagonal1 = 0
    max_diagonal2 = 0

    for i in range(100):
        row = 0
        col = 0
        max_diagonal1 += arr[i][i]
        max_diagonal2 += arr[i][99 - i]

        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]

        if row > max_row:
            max_row = row
        if col > max_col:
            max_col = col
        
    print("#{} {}".format(number, max(max_row, max_col, max_diagonal1, max_diagonal2)))

