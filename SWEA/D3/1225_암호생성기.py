from collections import deque

for test_case in range(10):
    T = int(input())

    data = list(map(int, input().split()))
    queue = deque(data)
    # 감소할 숫자
    i = 1

    while True:
        if i == 6:
            i = 1
        
        number = queue.popleft() - i
        if number <= 0:
            number = 0
            queue.append(number)
            break
        else:
            queue.append(number)
            i += 1

    print(f"#{T}", end = ' ')
    print(*queue)
