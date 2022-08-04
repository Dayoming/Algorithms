def solution(n):
    answer = ''
    while n > 0:
        # a triad notation
        remainder = n % 3
        n = n // 3
        answer += str(remainder)
    # the conversion of a triad to a decimal
    return int(answer, 3)


print(solution(125))
