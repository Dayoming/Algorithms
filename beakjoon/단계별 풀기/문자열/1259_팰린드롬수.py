# 팰린드롬수
import sys

while True:
    n = sys.stdin.readline().strip()
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')