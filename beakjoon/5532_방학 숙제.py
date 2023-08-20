l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c == 0:
    num1 = a // c
else:
    num1 = (a//c) + 1

if b % d == 0:
    num2 = b // d
else:
    num2 = (b//d) + 1

num = max(num1, num2)

print(l - num)