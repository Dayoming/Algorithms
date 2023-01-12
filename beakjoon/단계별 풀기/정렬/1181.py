# 단어 정렬
import sys

# 단어의 개수 n개 입력받기
n = int(sys.stdin.readline())
# 단어를 저장할 리스트 초기화
words = []

# 단어 입력받기
for i in range(n):
    words.append(sys.stdin.readline().strip())

# set으로 바꿔서 중복 제거 후 다시 list로 바꿔줌
words = list(set(words))
# 사전 순 정렬
words.sort()
# 길이 짧은 순 정렬
words.sort(key=len)

# 출력
for i in words:
    print(i)