# 에라토스테네스의 체, 이분탐색
import sys

def prime_list(n):
    prime = [False for _ in range(n + 1)]
    for i in range(2, n + 1):
        if prime[i] == False:
            for j in range(i + i, n + 1, i):
                prime[j] = True
    
    return [i for i in range(2, n + 1) if prime[i] == False]

n = int(sys.stdin.readline())
answer = 0

prime = prime_list(n)
left = 0
right = 1

while left < right:
    temp = sum(prime[left:right])
    # 오른쪽 포인터가 소수 리스트의 끝까지 도달하면 종료
    if right == len(prime) + 1:
        break
    # 연속된 소수의 합이 N과 같으면
    if temp == n:
        # 경우의 수를 더해주고 왼쪽 포인터 1 증가
        answer += 1
        left += 1
    # 연속된 소수의 합이 N보다 작으면
    elif temp < n:
        # 오른쪽 포인터 1 증가
        right += 1
    # 연속된 소수의 합이 N보다 크면
    elif temp > n:
        # 왼쪽 포인터 1 증가
        left += 1

print(answer)
    
