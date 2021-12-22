# 벌집
# layer로 찾기

import sys

def beehive(n):
    sum = 2
    layer = 1
    
    if n == 1:
        return 1
    
    while n >= sum:
        sum = sum + 6 * layer
        layer = layer + 1
    return layer

n = int(sys.stdin.readline())
print(beehive(n))
