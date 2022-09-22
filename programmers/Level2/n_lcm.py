# Find the least common multiple
def lcm(a, b):
    return (a * b) // gcd(a, b)


# Find the greatest common divisor
def gcd(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


def solution(arr):
    # Initialize answer
    answer = arr[0]
    for i in arr:
        answer = lcm(answer, i)
    return answer


print(solution([2, 6, 8, 14]))
