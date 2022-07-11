def solution(num):
    collatz_num = num
    cnt = 0
    while collatz_num != 1:  # If collatz_num's 1, it's over
        if cnt >= 500:  # If cnt exceeds 500 times, -1 will be returned
            cnt = -1
            break
        if collatz_num % 2 == 0:  # If collatz_num's an even number, collatz_num // 2
            collatz_num = collatz_num // 2
            cnt += 1
        else:
            # If collatz_num's an odd number, collatz_num * 3 + 1
            collatz_num = collatz_num * 3 + 1
            cnt += 1
    return cnt
