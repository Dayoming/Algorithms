def solution(n):
    x = 1  # a divisor of n
    while True:
        if n % x == 1:
            return x
        else:
            x += 1
    return answer
