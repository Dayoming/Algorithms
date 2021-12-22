# 두 정수와 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys

t = int(input())
result = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    s = "Case #" + repr(i + 1) + ": " + repr(a) + " + " + repr(b) + " = " + repr(a + b)
    result.append(s)

for j in result:
    print(j)
