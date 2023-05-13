# 0, 1, ?으로 구성된 문자 S와 N이 주어진다.
# ?는 각각 0과 1로 교체될 수 있는데,
# 이를 교체해서 얻을 수 있는 이진수들의 집합에서 정수 N 이하의 수를 출력한다.
import sys

s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
answer = -1
# 얻을 수 있는 이진수 집합
collection = []
# ?가 있는 index들 저장
indexes = [i for i, c in enumerate(s) if c == '?']
indexes.reverse()

# 제일 작은 수
collection.append(int(format(s.replace('?', '0')), 2))
# 만들 수 있는 제일 큰 수
collection.append(int(format(s.replace('?', '1')), 2))

binary = list(format(s.replace('?', '0')))

for i in indexes:
    binary[i] = '1'
    temp = int("".join(binary), 2)
    if temp < n:
        answer = temp
    else:
        break
    
print(answer)