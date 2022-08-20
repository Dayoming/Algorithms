def solution(number, k):
    answer = []
    for num in number:
        # While there is something in the answer,
        # k is greater than 0,
        # and the last value of the answer is less than the current num
        while answer and k > 0 and answer[-1] < num:
            # Remove answer's top value and k - 1
            answer.pop()
            k -= 1
        # The num value must be added in answer
        answer.append(num)

    # Answer is number's length - k slicing
    answer = ''.join(answer[:len(number)-k])
    return answer


print(solution("1924", 2))
