def solution(n):
    answer = ''  # Variables to store results
    for i in range(1, n + 1):
        if i % 2 != 0:  # If i is odd
            answer += '수'  # answer add '수'
        else:  # If i is even
            answer += '박'  # answer add '박'
    return answer


print(solution(3))
