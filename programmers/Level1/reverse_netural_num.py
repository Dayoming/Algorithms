def solution(n):
    temp = str(n)  # Replace natural numbers with characters
    answer = []
    for i in temp[::-1]:  # List reverse
        answer.append(int(i))
    return answer


print(solution(12345))
