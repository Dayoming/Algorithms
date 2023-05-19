T = int(input())

for test_case in range(T):
    # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지
    h, w, n = map(int, input().split())

    # 배정되어야 하는 방 층수 구하기
    if h == 1:
        # 1층이면 층수는 무조건 1층
        floor = 1
    else:
        # 층수가 h로 나누어 떨어지면 층수는 h와 같음
        if n % h == 0:
            floor = h
        else:
        # 나머지가 있으면 층수는 n을 h로 나눈 나머지
            floor = n % h

    # 몇 호, n이 h만큼 증가할 때마다 호수가 1씩 증가
    temp = floor
    room = 1

    while temp != n:
        room += 1
        temp += h
        
    
    print(floor * 100 + room)

    