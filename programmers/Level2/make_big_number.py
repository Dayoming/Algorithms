from itertools import combinations


def solution(number, k):
    answer = ''
    numbers = []
    # Find all combinations
    for i in combinations(number, len(number) - k):
        temp = ''.join(i)
        numbers.append(int(temp))
    answer = str(max(numbers))
    return answer


print(solution("1924", 2))
