import sys

s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())

# @를 대체할 수 있는 카드들
cards = ['a', 't', 'c', 'o', 'd', 'e', 'r']

# 만약 @를 제외한 나머지 문자열이 같다면 통과


# 만약 @를 제외한 나머지 문자열이 다르고, 
# 다른 문자열을 cards 안에서 만들 수 있으면 통과
s.sort()
t.sort()

print(s)
print(t)