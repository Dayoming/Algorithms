import sys

t = int(sys.stdin.readline())

for _ in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    even = []
    
    for i in nums:
        if i % 2 == 0:
            even.append(i)
    
    print(sum(even), min(even))