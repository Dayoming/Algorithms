import sys

n, m = map(int, sys.stdin.readline().strip().split())
memo = {}

for i in range(n):
    address, pw = sys.stdin.readline().strip().split()
    memo[address] = pw

for j in range(m):
    find_address = sys.stdin.readline().strip()
    print(memo[find_address])