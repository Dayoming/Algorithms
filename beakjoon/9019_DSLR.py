import sys
from collections import deque

# D는 n을 두 배로 바꾸고 결과 값이 9999보다 큰 경우에는 10000으로 나눈 나머지를 취함
# 결과 값을 레지스터에 저장

# S는 n에서 1을 뺀 결과 n-1을 레지스터에 저장
# n이 0이라면 9999가 대신 레지스터에 저장
    
# L은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장
# R은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    queue = deque()
    visited = [False for _ in range(10000)]
    
    queue.append((a, ''))
    
    while queue:
        n, command = queue.popleft()
        visited[n] = True
        
        # 만약 n이 결과값이면
        if n == b:
            print(command)
            break
            
        temp = (2 * n) % 10000
        # 만약 방문하지 않은 수면
        if not visited[temp]:
            queue.append((temp, command + 'D'))
            visited[temp] = True
        
        temp = (n - 1) % 10000
        if not visited[temp]:
            queue.append((temp, command + 'S'))
            visited[temp] = True
        
        temp = (10 * n + (n // 1000)) % 10000
        if not visited[temp]:
            queue.append((temp, command + 'L'))
            visited[temp] = True
            
        # 4
        temp = (n // 10 + (n % 10) * 1000) % 10000
        if not visited[temp]:
            queue.append((temp, command + 'R'))
            visited[temp] = True