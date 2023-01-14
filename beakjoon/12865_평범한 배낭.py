# 평범한 배낭
import sys

# 초기 리스트 K 초기화
def init_K(n, M):
    K = [[None]*(M + 1) for _ in range(n + 1)] # 초기 리스트 선언
    for w in range(M+1): # 초기행의 경계값 0으로 설정
        K[0][w] = 0
    for i in range(n+1): # 초기열의 경계값 0으로 설정
        K[i][0] = 0
    return K

# n은 물건의 개수, M은 배낭 용량, W와 P는 각각 물건의 무게와 이익을 담은 배열
def DP1(n, M, W, P):
    K = init_K(n, M) # 초기 리스트 선언
    for i in range(1, n + 1): # 1행부터 n행까지 반복
        for w in range(1, M + 1): # 1행부터 M열까지 반복
            if (w < W[i - 1]): # 배낭이 찢어지는 경우
                K[i][w] = K[i - 1][w] # 이전 행 w 위치와 동일하게 삽입
            else:
                # K의 index는 0~5고, W, P 배열은 index가 0~4기 때문에 index out of range를 방지하기 위해 i - 1을 해준다
                # 이전 행의 두 값과 비교하고 큰 값을 삽입
                K[i][w] = max(K[i - 1][w], K[i - 1][w-W[i - 1]]+P[i - 1])
    return K # 배열 K를 반환

n, k = map(int, sys.stdin.readline().split())
W = [] # 물건의 무게를 담은 배열
P = [] # 물건의 이익을 담은 배열

for i in range(n):
    weight, profit = map(int, sys.stdin.readline().split())
    W.append(weight)
    P.append(profit)

print(DP1(n, k, W, P)[n][k])