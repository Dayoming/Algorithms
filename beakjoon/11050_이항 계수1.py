n, k = map(int, input().split())

def factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

print(factorial(n) // ((factorial(n - k) * factorial(k))))