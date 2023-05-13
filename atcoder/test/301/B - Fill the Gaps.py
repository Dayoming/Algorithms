n = int(input())
sequence = list(map(int, input().split()))
answer = [sequence[0]]

for i in range(1, len(sequence)):
    # 만약 다음 수가 큰 수인 경우
    if sequence[i] > answer[-1]:
        # 두 수가 같아질 때까지 계속 증가
        while sequence[i] != answer[-1]:
            answer.append(answer[-1] + 1)
    
    # 만약 다음 수가 작은 수인 경우
    if sequence[i] < answer[-1]:
        # 두 수가 같아질 때까지 계속 감소
        while sequence[i] != answer[-1]:
            answer.append(answer[-1] - 1)

print(*answer)
        
        