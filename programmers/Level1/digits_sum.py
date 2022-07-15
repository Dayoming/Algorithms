def solution(n):
    answer = 0  # Cumulative number
    for digits in str(n):  # Replace with string and repeat
        answer += int(digits)  # Replace with integer and sum

    return answer
