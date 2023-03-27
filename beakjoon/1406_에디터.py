import sys

# 문자열을 담을 첫 번째 스택
string = list(sys.stdin.readline().rstrip())
# 이후의 문자열을 담을 두 번째 스택
string2 = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rstrip().split()

    # L인 경우 커서를 왼쪽으로 한 칸 옮김(문장의 맨 앞이면 무시)
    if command[0] == 'L':
        # 만약 첫 번째 스택이 비어있지 않으면
        if string:
            # 첫 번째 스택의 마지막 값을 삭제하고 두 번째 스택의 마지막에 넣어줌
            string2.append(string.pop())
    # D인 경우 커서를 오른쪽으로 한 칸 옮김(문장의 맨 뒤면 무시)
    elif command[0] == 'D':
        # 만약 두 번째 스택이 비어있지 않으면
        if string2:
            # 두 번째 스택의 마지막 값을 삭제하고 첫 번째 스택의 마지막에 넣어줌
            string.append(string2.pop())
    # B인 경우 커서 왼쪽에 있는 문자를 삭제(문장의 맨 앞이면 무시)
    elif command[0] == 'B':
        if string:
            string.pop()
    # 커서 왼쪽에 문자 추가
    elif command[0] == 'P':
        string.append(command[1])

print(''.join(string + string2[::-1]))