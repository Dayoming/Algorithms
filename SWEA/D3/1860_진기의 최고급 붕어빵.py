# 테스트 케이스의 수 T
T = int(input())

for test_case in range(1, T + 1):
    # 자격을 얻은 사람의 수 n, 붕어빵을 만드는 시간 m, 만들어지는 개수 k
    n, m, k = map(int, input().split())
    # 손님들이 언제 도착하는지 초 단위로 나타냄
    guest = list(map(int, input().split()))
    guest.sort()
    switch = True
    
    for i in range(n):
        # 총 빵의 개수는 손님이 도착한 도착한 시간 // 붕어빵 만드는 시간 * 만들어지는 개수
        total_bread = (guest[i] // m) * k
        
        # 만약 총 빵의 개수가 현재 인원수보다 작다면
        if total_bread < i + 1:
            switch = False
            break
    
    if switch:
        print("#{} Possible".format(test_case))
    else:
        print("#{} Impossible".format(test_case))