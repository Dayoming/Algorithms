def solution(price, money, count):
    result = 0  # Initialize result
    for i in range(1, count + 1):  # Repeat by count
        result += price * i  # Sum price * count

    if money - result < 0:  # If money - result is negative number
        result = abs(money - result)
    else:  # If money - result is positive number
        result = 0
    return result


print(solution(3, 20, 4))
