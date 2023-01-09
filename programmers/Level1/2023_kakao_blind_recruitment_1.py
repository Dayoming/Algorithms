# 개인정보 수집 유효기간
from datetime import datetime

def solution(today, terms, privacies):
    # 결과를 저장할 배열
    answer = []
    # 각 약관별 유효기간을 저장할 딕셔너리
    term = {}
    # 오늘 날짜 today를 날짜 객체로 변환
    today = datetime.strptime(today, '%Y.%m.%d')

    # 약관별 유효기간 저장
    for i in range(len(terms)):
        term_name, month = terms[i].split()
        term[term_name] = int(month)
    
    # 유효기간이 지났는지 확인하는 반복문
    for i in range(len(privacies)):
        # 개인정보 수집 일자를 공백으로 구분해 입력받고 날짜 객체로 변환
        collection = datetime.strptime(privacies[i].split()[0], '%Y.%m.%d')
        
        # 일 수는 해당하는 약관의 유효기간 * 28(한 달이 28일이라 가정했으므로)
        day = term.get(privacies[i].split()[1]) * 28
        # 수집 일자의 연도
        year = collection.year
        # 수집 일자의 달
        month = collection.month
        # 수집 일자의 일 수
        ex_day = collection.day

        # 일 수가 0이 될 때까지 반복
        while day != 0:
            # 만약 12월 28일이면 다음 연도로 넘겨주고 1월 1일로 초기화
            if month == 12 and ex_day == 28:
                year += 1
                month = 1
                ex_day = 1
            # 28일이면 다음 달로 넘겨주고 1일로 초기화
            elif ex_day == 28:
                month += 1
                ex_day = 1
            # 두 경우 다 아니면 하루 증가
            else:
                ex_day += 1
            # 일 수 1 감소
            day -= 1
        # 만료 날짜(보관 가능한 마지막 날짜 다음 일자를 저장)
        expiration = datetime(year, month, ex_day)
        # 만료 날짜가 오늘보다 작거나 같으면 answer에 해당 인덱스 + 1 저장
        if expiration <= today:
            answer.append(i + 1)
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))