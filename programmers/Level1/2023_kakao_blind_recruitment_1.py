# 개인정보 수집 유효기간
from datetime import timedelta
from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    term = {}
    today = datetime.strptime(today, '%Y.%m.%d')
    for i in range(len(terms)):
        term_name, month = terms[i].split()
        term[term_name] = int(month)
    
    for i in range(len(privacies)):
        collection = datetime.strptime(privacies[i].split()[0], '%Y.%m.%d')
        day = term.get(privacies[i].split()[1]) * 28
        year = collection.year
        month = collection.month
        ex_day = collection.day
        while day != 0:
            if month == 12 and ex_day == 28:
                year += 1
                month = 1
                ex_day = 1
            elif ex_day == 28:
                month += 1
                ex_day = 1
            else:
                ex_day += 1
            day -= 1
        expiration = datetime(year, month, ex_day)
        if expiration <= today:
            answer.append(i + 1)
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))