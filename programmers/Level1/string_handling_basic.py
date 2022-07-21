def solution(s):
    answer = False  # Variables to store results
    if (len(s) == 4 or len(s) == 6) and s.isdigit():  # If string length is 4 or 6, and it's number
        answer = True
    return answer
