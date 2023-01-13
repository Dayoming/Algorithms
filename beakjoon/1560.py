# 비숍
import sys

n = int(sys.stdin.readline().strip())

# 그림을 그렸을 때, 항상 n + (n - 2) 개의 비숍이 배치되는 것을 확인할 수 있다
if n <= 2:
    print(n)
else:
    print(n + (n - 2))