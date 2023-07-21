class Solution(object):
    def intToRoman(self, num):
        answer = ''
        symbols_count = [0, 0, 0, 0, 0, 0, 0]
        symbols_values = [1000, 500, 100, 50, 10, 5, 1]
        idx = 0
        
        # 각각 숫자를 만드는데 필요한 symbol 개수를 구한다
        while num != 0:
            if num >= symbols_values[idx]:
                num -= symbols_values[idx]
                symbols_count[idx] += 1
            else:
                idx += 1
        
        # 각 symbol의 개수별로 문자열 합치기
        # num의 범위가 3999까지이므로, M은 3개가 최대 -> 4개 이상일 경우 고려해줄 필요 X
        answer += 'M' * symbols_count[0]
        # 만약 500이 1개, 100이 4개 있으면 CM 추가 (900인 경우)
        if symbols_count[1] == 1 and symbols_count[2] == 4:
            answer += 'CM'
        # 만약 100이 4개 있으면 CD 추가
        elif symbols_count[2] == 4:
            answer += 'CD'
        # 그렇지 않으면 각각 D와 C의 개수만큼 추가
        else:
            answer += 'D' * symbols_count[1]
            answer += 'C' * symbols_count[2]
        # 만약 50이 1개, 10이 4개 있으면 XC 추가 (90인 경우)
        if symbols_count[3] == 1 and symbols_count[4] == 4:
            answer += 'XC'
        # 만약 10이 4개 있으면 XL 추가 (40인 경우)
        elif symbols_count[4] == 4:
            answer += 'XL'
        # 그렇지 않으면 각각 L과 X의 개수만큼 추가
        else:
            answer += 'L' * symbols_count[3]
            answer += 'X' * symbols_count[4]
        
        # 만약 10이 1개, 1이 9개 있으면 IX 추가 (9인 경우)
        if symbols_count[5] == 1 and symbols_count[6] == 4:
            answer += 'IX'
        # 만약 1이 4개 있으면 IV 추가 (4인 경우)
        elif symbols_count[6] == 4:
            answer += 'IV'
        else:
            answer += 'V' * symbols_count[5]
            answer += 'I' * symbols_count[6]
            
        return answer

s = Solution()
print(s.intToRoman(58))
print(s.intToRoman(1994))
print(s.intToRoman(3))