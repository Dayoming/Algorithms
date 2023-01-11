# 나는야 포켓몬 마스터 이다솜
import sys

# sys.stdin.readline()으로 입력 시간 줄이기
n, m = map(int, sys.stdin.readline().split())
pokemon = {}

for i in range(1, n + 1):
    pokemon[i] = input()

# key와 value가 뒤집어진 딕셔너리 생성
reverse_pokemon = dict(map(reversed, pokemon.items()))

for i in range(m):
    # sys.stdin.readline()으로 입력 시간 줄이고 문자열 시작과 끝의 공백 삭제(개행문자 삭제)
    question = sys.stdin.readline().strip()
    # 만약 숫자라면 포켓몬 이름 출력
    if question.isnumeric():
        print(pokemon[int(question)])
    # 문자라면 도감 번호 출력
    else:
        print(reverse_pokemon[question])