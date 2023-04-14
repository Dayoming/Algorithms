
T = int(input())
for test_case in range(T):
    n = int(input())

    # 0의 출현 개수 저장
    cnt0 = [1, 0]
    # 1의 출현 개수 저장
    cnt1 = [0, 1]

    # 0이면 1 0, 1이면 0 1 출력
    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")
    else:
        # 2부터는 n - 1과 n - 2의 합을 더해줌
        for i in range(2, n + 1):
            cnt0.append(cnt0[i - 1] + cnt0[i - 2])
            cnt1.append(cnt1[i - 1] + cnt1[i - 2])
        print(f"{cnt0.pop()} {cnt1.pop()}")