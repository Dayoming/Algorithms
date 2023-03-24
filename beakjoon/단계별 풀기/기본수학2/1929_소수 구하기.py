# 에라토스테네스의 체
def prime_list(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [2]
    sieve = [True] * (n + 1)
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int((n + 1) ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n + 1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n + 1) if sieve[i] == True]

# M부터 N까지의 모든 소수 출력하기
m, n = map(int, input().split())

answer = prime_list(n)

for i in answer:
    if i >= m and i <= n:
        print(i)

