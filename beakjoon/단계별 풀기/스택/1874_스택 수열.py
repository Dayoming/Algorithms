# 스택 수열
import sys

n = int(sys.stdin.readline())
# [8, 7, 6, 5, 4, 3, 2, 1] 과 같이 내림차순 형태로 수열 생성
numbers = [i for i in range(n, 0, -1)]
# 입력된 수열을 저장할 스택
stack = []
# 수열을 만들기 위해 임시로 저장할 스택
answer = [0]
# 수열을 만들기 위해 필요한 연산을 저장할 스택
command = []
# 스택의 index
index = 0


for i in range(n):
    stack.append(int(sys.stdin.readline()))

# 입력받은 수열 내림차순으로 정렬
stack.reverse()

# 수열이 만들어질 때까지 반복
while len(stack) != 0:
    # 만약 answer의 마지막 값이 stack의 마지막 값과 같지 않으면
    if answer[index] != stack[-1]:
        # stack의 마지막 수와 answer의 마지막 수가 같지 않은데
        # 더 이상 넣을 수 있는 number의 값이 없는 경우
        if len(numbers) == 0:
            command.clear()
            command.append("NO")
            break
        # answer에 numbers의 마지막 값을 넣고
        # command에 +를 넣는다.
        else:
            answer.append(numbers.pop())
            command.append('+')
            index += 1
    # answer의 마지막 값과 stack의 마지막 값이 같으면
    else:
        # stack의 마지막 값과 answer의 마지막 값을 지우고 command에 -를 더한다.
        # answer가 하나 줄게 되므로 index도 -1 해준다.
        stack.pop()
        answer.pop()
        command.append('-')
        index -= 1

for j in command:
    print(j)
