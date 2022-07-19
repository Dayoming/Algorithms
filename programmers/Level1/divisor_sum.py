def solution(n):
    answer = 0  # Variables to store results
    for i in range(1, n + 1):  # Repeat from 1 to n
        if n % i == 0:  # If it's divided,
            answer += i
    return answer
