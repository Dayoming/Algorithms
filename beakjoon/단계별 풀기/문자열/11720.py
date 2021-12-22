# 숫자의 합
# N개의 숫자가 공백없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

n = int(input())
numbers = input()
result = 0

for i in numbers:
    result = result + int(i)

print(result)