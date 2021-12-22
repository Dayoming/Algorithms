# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
import sys

n = int(sys.stdin.readline())
sequence = map(int, sys.stdin.readline().split())
result = []

for i in sequence:
    result.append(i)

result.sort()

print(result[0], result[-1])