def solution(numbers):
    # List to store results
    answer = []
    # Repeat as many times as numbers
    for i in range(0, len(numbers)):
        # Repeat as many times as i + 1 to numbers
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    # Deduplication
    answer = list(set(answer))
    answer.sort()
    return answer


print(solution([5, 0, 2, 7]))
