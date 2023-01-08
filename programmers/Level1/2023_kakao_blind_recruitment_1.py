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
        expiration = datetime.strptime(privacies[i].split()[0], '%Y.%m.%d')
        expiration = expiration + timedelta(days=(term.get(privacies[i].split()[1])) * 28)
        print(expiration)
        if today > expiration:
            answer.append(i + 1)
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))