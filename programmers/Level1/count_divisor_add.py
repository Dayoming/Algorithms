def solution(left, right):
    # Initialize answer
    answer = 0
    # Store count dictionary
    count = {}
    for i in range(left, right + 1):
        # count[key] value initialize
        count[i] = 0
        for j in range(1, i + 1):
            # If j is divisor
            if i % j == 0:
                # divisor count + 1
                count[i] += 1

    # Repeat dictionary key
    for key in count:
        # If count[key] value is even
        if count[key] % 2 == 0:
            answer += key
        # If count[key] value is odd
        else:
            answer -= key
    return answer


print(solution(13, 17))
