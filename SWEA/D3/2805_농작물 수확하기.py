T = int(input())

for test_case in range(T):
    # 농장의 크기 입력받기
    n = int(input())
    farm = []
    for _ in range(n):
        farm.append(list(map(int, input())))

    # 수확 시작 위치 정하기
    start = n // 2
    # 시작 개수 정하기
    count = 1
    answer = 0
    reverse = False

    for i in range(len(farm)):
        # 수확 시작 위치부터 개수만큼 더해준다
        if count == n:
            reverse = True

        for j in range(count):
            answer += farm[i][start + j]

        if reverse:
            count -= 2
            start += 1
        else:
            count += 2
            start -= 1

    print("#{} {}".format(test_case + 1, answer))
        
        
        


