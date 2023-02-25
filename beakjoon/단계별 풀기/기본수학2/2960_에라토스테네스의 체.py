# 수학, 구현, 정수론, 소수 판정, 에라토스테네스의 체

def get_prime(N, K):
    count = 0
    arr = [True] * (N + 1)
    for i in range(2, N + 1):
        if arr[i] == True: # 만약 i가 소수라면
            for j in range(i, N + 1, i):
                # 이미 지워진 수가 아니라면
                if arr[j] != False:
                    arr[j] = False
                    count += 1
                if count == K:
                    return(j)

N, K = map(int, input().split())
print(get_prime(N, K))