# 숫자 카드 2
import sys

n = int(sys.stdin.readline())
have_cards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

hash = {}

for i in have_cards:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in cards:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')