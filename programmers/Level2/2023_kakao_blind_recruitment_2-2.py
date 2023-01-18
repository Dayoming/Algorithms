# 이모티콘 할인행사
from itertools import product

def solution(users, emoticons):
    answer = [0, 0] # 플러스 가입 수, 이모티콘 매출액
    discounts = [10, 20, 30, 40]
    
    for discount in product(discounts, repeat=len(emoticons)):
        total_pay, plus_num = 0, 0
        for rate, price in users:
            pay = 0
            for i, emoticon in enumerate(emoticons):
                if discount[i] >= rate:
                    pay += emoticon * (100 - discount[i]) // 100
            if pay >= price: # 이모티콘 구매를 모두 취소하고 플러스 가입
                plus_num += 1
            else: # 이모티콘 플러스에 가입하지 않는 경우
                total_pay += pay
            
        if plus_num > answer[0]: # 이모티콘 플러스 가입자 수가 증가한 경우
            answer[0], answer[1] = plus_num, total_pay
        elif plus_num == answer[0] and total_pay > answer[1]: # 플러스 가입자 수는 같으면서 매출액은 증가
            answer[1] = total_pay

    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))