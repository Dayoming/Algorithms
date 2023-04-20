import sys
import heapq

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    x = int(sys.stdin.readline())
    # 입력받은 정수가 0이 아니면
    if x != 0:
        heapq.heappush(queue, (abs(x), x))
    else:
        if not queue:
            print(0);
        else:
            print(heapq.heappop(queue)[1])