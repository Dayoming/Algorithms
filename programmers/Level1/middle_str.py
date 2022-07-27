def solution(s):
    answer = ''  # Initialize answer
    str_length = len(s)  # Store string length
    if str_length % 2 == 0:  # If even
        # Ex) "qwer" -> s[1:3] -> "we"
        answer = s[str_length // 2 - 1:str_length // 2 + 1]
    else:  # If odd
        answer = s[str_length // 2]
    return answer
