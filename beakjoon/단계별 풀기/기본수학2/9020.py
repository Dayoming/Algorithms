# 골드바흐의 추측

# 에라토스테네스의 체
def prime_list(n):
    sieve = [True] * n
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def goldbach_number(number):
    prime = prime_list(number)
    goldbach = {}
    for i in prime:
        for j in prime:
            if i + j == number:
                goldbach[max(i, j) - min(i, j)] = [i, j]
    print(*goldbach[min(goldbach.keys())])

n = int(input()) # 입력받을 수의 개수
for i in range(n):
    number = int(input())
    goldbach_number(number)
