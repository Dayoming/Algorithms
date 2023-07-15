# 요리의 개수 n, 음료 정상가 p, 쿠폰 할인가 q
n, p, q = map(int, input().split())
# 요리 가격
d = list(map(int, input().split()))
# 할인가 저장 리스트
sales = []

# 음료만 사는게 더 싼지, 요리를 하나 더 사서 할인받는게 싼지 비교
min_amount = min(q + i for i in d) if d else p

print(min(min_amount, p))