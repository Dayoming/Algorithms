# 괄호

def check_vps(ps):
    temp = []
    for i in ps:
        if i == '(':
            temp.append(i)
        else:
            if len(temp) == 0 or temp[-1] == ')':
                temp.append(i)
            else:
                temp.pop(-1)

    if len(temp) == 0:
        print('YES')
    else:
        print('NO')

n = int(input())

for i in range(n):
    # Input Parenthesis String
    ps = input()
    check_vps(ps)

