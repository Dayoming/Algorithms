def solution(n):
    f_zero, f_one = 0, 1
    for i in range(n - 1):
        f_zero, f_one = f_one, f_zero + f_one
    return f_one % 1234567
