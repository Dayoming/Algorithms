def solution(a, b):
    answer = 0  # Initialize answer
    temp = 0  # Initialize temp
    if a > b:  # To repeat from small to large numbers
        temp = b
        b = a
        a = temp
    for i in range(a, b + 1):
        answer += i
    return answer
