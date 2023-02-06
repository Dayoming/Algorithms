# 균형잡힌 세상
import sys


while True:
    s = sys.stdin.readline().rstrip()
    brackets = []
    
    if s == '.':
        break
    for i in s:
        # 만약 여는 괄호라면
        if i == '[':
            # 스택에 더해준다
            brackets.append(i)
        elif i == '(':
            brackets.append(i)
        
        # 닫는 괄호라면
        if i == ']':
            # 스택에 이미 괄호가 존재하는 상태
            if brackets and brackets[-1] == '[':
                # 이전 괄호를 없애준다.
                brackets.pop()
            else:
                brackets.append(i)
        if i == ')':
            if brackets and brackets[-1] == '(':
                brackets.pop()
            else:
                brackets.append(i)
        
    if brackets:
        print('no')
    else:
        print('yes')


