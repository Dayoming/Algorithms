import sys
from collections import deque

# 테스트 케이스의 개수
t = int(sys.stdin.readline())

for _ in range(t):
    # 수행할 함수
    p = sys.stdin.readline().rstrip()
    # 배열에 들어있는 수의 개수
    n = int(sys.stdin.readline())
    # 배열에 들어있는 정수
    arr = deque(sys.stdin.readline().rstrip().split(','))
    arr[0] = arr[0].replace('[', '')
    arr[-1] = arr[-1].replace(']', '')
    
    flag = True
    empty = False

    for command in p:
        # 비어있으면 [] 비어있는 상태에서 D면 에러로 고치기 ~~~
        # 뒤집기 ~~~
        # arr이 비어있으면 error
        if (not arr and command == 'D') or (arr == deque(['']) and command == 'D'):
            print("error")
            empty = True
            break
        elif command == 'R':
            if flag == True:
                flag = False
            else:
                flag = True
        # flag가 정방향이면
        elif command == 'D' and flag:
            arr.popleft()
        elif command == 'D' and not flag:
            arr.pop()
        
    # flag가 정방향이면
    if not empty:
        if flag:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')
            