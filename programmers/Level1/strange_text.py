def solution(s):
    answer = ''  # Variables to store answers
    cnt = 0  # Index of characters
    for i in range(len(s)):
        if s[i] == ' ':  # If it's space
            answer += ' '
            cnt = 0
            continue
        if cnt % 2 == 0:  # If it's even
            answer += s[i].upper()
            cnt += 1
        else:  # If it's odd
            answer += s[i].lower()
            cnt += 1
    return answer
