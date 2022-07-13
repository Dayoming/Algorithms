def solution(n):
    square_root = n ** (1/2)  # Square root
    temp = int(square_root)
    # 1.1234 - 1 = 0.1234... is not integer
    if square_root - temp == 0:  # If temp is don't have a decimal point
        answer = (int(square_root) + 1) ** 2
    else:
        answer = -1
    return answer


print(solution(3))
