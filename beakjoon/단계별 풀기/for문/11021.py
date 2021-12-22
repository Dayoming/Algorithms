# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys

t = int(input())
result = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a + b)

for j in range(len(result)):
    s = 'Case #' + repr(j + 1) + ': ' + repr(result[j])
    print(s)