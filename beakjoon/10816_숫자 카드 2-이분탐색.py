# 숫자 카드 2
import sys

# 이분탐색
def binary_search(target, data):
    left = 0
    right = len(data) - 1
    # 몇 개가 있는지 셀 변수 초기화
    cnt = 0

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            # 탐색한 수가 target과 같으면 cnt + 1
            cnt += 1
            # 해당하는 인덱스의 값을 리스트에서 삭제
            del data[mid]
            # 값이 하나 삭제되었으므로 right - 1
            right = right - 1
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return cnt

n = int(sys.stdin.readline())
have_cards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

# cards의 값이 중복되는 경우(1, 1, 2, 2 등)를 처리하기 위해 cnts를 딕셔너리로 선언
cnts = dict.fromkeys(cards)

have_cards.sort()

for i in cnts:
    cnts[i] = (binary_search(i, have_cards))

for j in cards:
    print(cnts[j], end=' ')