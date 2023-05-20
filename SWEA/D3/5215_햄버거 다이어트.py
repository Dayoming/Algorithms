def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]

t = int(input())

for test_case in range(1, t + 1):
    # 재료의 수, 제한 칼로리
    n, l = map(int, input().split())
    
    # 점수(이익)
    profit = []
        
    # 칼로리(비용)
    weight = []

    # 주어진 제한 칼로리 이하의 조합 중 가장 맛에 대한 점수가 높은 햄버거의 점수 출력
    for _ in range(n):
        # 맛에 대한 점수, 칼로리
        t, k = map(int, input().split())
        
        profit.append(t)
        weight.append(k)
        
    
    print("#{} {}".format(test_case, knapSack(l, weight, profit, n)))
        
        
        