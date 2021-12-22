# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
# 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.

# 1사분면(1, 1), 2사분면(-1, 1), 3사분면(-1, -1), 4사분면(1, -1)

x = int(input())
y = int(input())
result = 0

if x > 0:
    if y < 0:
        result = 4
    elif y > 0:
        result = 1
elif x < 0:
    if y < 0:
        result = 3
    elif y > 0:
        result = 2

print(result)