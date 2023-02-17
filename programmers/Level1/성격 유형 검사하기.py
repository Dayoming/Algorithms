# 2022 KAKAO TECH INTERNSHIP
def solution(survey, choices):
    answer = ''
    personality = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    for i in range(len(survey)):
        # 검사자가 선택한 질문의 선택지가 비동의 쪽이면
        if choices[i] == 1:
            personality[survey[i][0]] += 3
        elif choices[i] == 2:
            personality[survey[i][0]] += 2
        elif choices[i] == 3:
            personality[survey[i][0]] += 1
        # 검사자가 선택한 질문의 선택지가 동의 쪽이면
        if choices[i] == 5:
            personality[survey[i][1]] += 1
        elif choices[i] == 6:
            personality[survey[i][1]] += 2
        elif choices[i] == 7:
            personality[survey[i][1]] += 3
    
    if personality['R'] < personality['T']:
        answer += 'T'
    else:
        answer += 'R'
    
    if personality['C'] < personality['F']:
        answer += 'F'
    else:
        answer += 'C'
    
    if personality['J'] < personality['M']:
        answer += 'M'
    else:
        answer += 'J'

    if personality['A'] < personality['N']:
        answer += 'N'
    else:
        answer += 'A'

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
print(solution(["AN", "CF", "MJ", "AN", "NA"], [4, 4, 4, 4, 4]))