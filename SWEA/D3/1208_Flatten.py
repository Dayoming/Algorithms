for i in range(10):
    # 덤프 횟수
    n = int(input())
    height = list(map(int, input().split()))

    # 주어진 덤프 횟수가 완료될 때까지
    while n != 0:
        # 만약 리스트의 최고점과 최저점의 차가 1보다 크거나 같다면
        if max(height) - min(height) >= 1:
            # 최고점과 최저점의 간격을 줄여준다
            height[height.index(max(height))] -= 1
            height[height.index(min(height))] += 1
        else:
            # 최고점과 최저점의 차가 1 이내가 된다면 종료
            break
        # 수행을 마지면 덤프 횟수 - 1
        n -= 1

    print('#{} {}'.format(i + 1, max(height) - min(height)))