import sys

t = int(sys.stdin.readline())

for _ in range(t):
    bin1, bin2 = sys.stdin.readline().split()
    print(str(bin(int('0b'+bin1, 2) + int('0b'+bin2, 2))).replace('0b', ''))