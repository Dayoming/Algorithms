def solution(absolutes, signs):
    # Initialize variable result
    result = 0
    for i in range(0, len(signs)):
        if signs[i] == False:
            # Change a Negative number to a positive number
            absolutes[i] = absolutes[i] * -1

    # Sum absolutes
    for i in absolutes:
        result += i
    return result


print(solution([1, 2, 3], [False, False, True]))
