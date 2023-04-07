t = int(input())
for _ in range(t):
    case = list(input().split())
    answer = ''
    for i in case:
        answer += i[::-1]
        answer += ' '

    print(answer)