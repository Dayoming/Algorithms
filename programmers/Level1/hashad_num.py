def solution(x):
    divide = 0  # Store values to divide
    for num in str(x):  # Repeat as many digits as possible
        divide += int(num)
    if x % divide == 0:
        answer = True
    else:
        answer = False
    return answer
