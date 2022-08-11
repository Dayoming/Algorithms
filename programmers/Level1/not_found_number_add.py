def solution(numbers):
    # Initialize variable result
    result = 0
    # 0~9 integer array
    range_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # If range_numbers not in number then result + i
    for i in range_numbers:
        if i not in numbers:
            result += i
    return result
