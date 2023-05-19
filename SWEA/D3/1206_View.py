# 테스트 케이스는 10으로 고정
for test_case in range(1, 11):
    
    n = int(input())
    answer = 0
    buildings = list(map(int, input().split()))
    
    for i in range(2, n - 2):
        maximum = max(buildings[i - 2], max(buildings[i - 1], max(buildings[i + 1], buildings[i + 2])))
        if buildings[i] - maximum > 0:
            answer += buildings[i] - maximum

    print("#{} {}".format(test_case, answer))
                          