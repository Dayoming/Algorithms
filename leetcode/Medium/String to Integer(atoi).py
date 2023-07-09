class Solution:
    def myAtoi(self, s: str) -> int:
        string = list(s)
        answer = ''
        numbers = ''
        idx = 0
        
        # 문자열이 공백으로 이루어졌거나 아무것도 없으면 0 반환
        if s.replace(' ', '') == '' or s == '':
            return 0
        
        # Step 1 선행 공백을 무시하기 위해 공백이 아닐 때까지 문자열 인덱스를 증가시킨다.
        while string[idx] == ' ':
            idx += 1
        
        # Step 2 -나 +가 있는지 찾고, 없으면 기존 인덱스를 사용한다.
        # idx가 string의 길이와 같아지면(끝까지 찾을 수 없었으면) idx를 1 줄여서 out of range 방지
        # 찾은 문자열을 읽는다 -> answer에 추가
        while idx == len(string) or string[idx] == '+' or string[idx] == '-':
            if idx == len(string):
                idx -= 1
                break
            answer += string[idx]
            idx += 1
        
        # 찾은 부호가 두 개 이상이면 0 반환
        if len(answer) > 1:
            return 0
        
        # Step 3 만약 찾은 부호 다음이 숫자면, 문자가 숫자인 동안만 읽는다.
        if string[idx].isdigit():
            for i in range(idx, len(string)):
                if str(string[i]).isdigit():
                    numbers += string[i]
                else:
                    idx = i
                    break
        # 부호 다음이 숫자가 아니면 0을 반환한다.
        else:
            return 0
            
        # Step 4 만약 읽어온 숫자가 있다면, 문자열을 정수로 변환 후 부호 붙여주기
        if numbers:
            numbers = int(numbers)
            answer = int(answer + str(numbers))
        # 읽어온 숫자가 없다면 answer는 0 반환
        else:
            return(0)
        
        # Step 5 32비트 부호 있는 정수 범위인지 확인하고 범위 내 수로 설정해주기
        if answer < -(2**31):
            answer = -(2**31)
        elif answer > 2**31 - 1:
            answer = 2**31 - 1
            
        return answer
    
s = Solution()
print(s.myAtoi("+"))
print(s.myAtoi("   -42"))
print(s.myAtoi("42"))
print(s.myAtoi("    57"))
print(s.myAtoi("words and 987"))
print(s.myAtoi(""))
