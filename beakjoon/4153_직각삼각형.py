# 직각삼각형
import sys

# 피타고라스 정리로 직각삼각형이 맞는지 검사
# 한 변의 제곱이 나머지 두 변의 제곱과 같은 경우 True 반환
def pythagoras(a, b, c):
    if a ** 2 == (b ** 2 + c ** 2):
        return True


while True:
    answer = []
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 0 and b == 0 and c == 0:
        break

    answer.append(pythagoras(a, b, c))
    answer.append(pythagoras(b, c, a))
    answer.append(pythagoras(c, a, b))

    if True in answer:
        print('right')
    else:
        print('wrong')