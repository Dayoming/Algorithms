# 최소 힙
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        # 0이 아니면 힙에 입력받은 정수를 넣는다
        heapq.heappush(heap, x)
    else:
        # 힙에 아무것도 들어있지 않은데 0이 입력되면 0을 출력
        if len(heap) == 0:
            print(0)
        else:
            # 힙에 원소가 존재하고 0이 입력되면 가장 작은 원소를 출력하고 삭제
            print(heapq.heappop(heap))
