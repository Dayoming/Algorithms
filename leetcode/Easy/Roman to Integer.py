class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        symbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        idx = 0
        
        # 다음 자리 숫자가 있는 동안 판별
        while idx < len(s):
            if idx + 1 < len(s):
                # 4와 9를 만드는 경우
                if s[idx] == 'I' and s[idx + 1] == 'V':
                    answer += 4
                    idx += 1
                elif s[idx] == 'I' and s[idx + 1] == 'X':
                    answer += 9
                    idx += 1
                # 40과 90을 만드는 경우
                elif s[idx] == 'X' and s[idx + 1] == 'L':
                    answer += 40
                    idx += 1
                elif s[idx] == 'X' and s[idx + 1] == 'C':
                    answer += 90
                    idx += 1
                # 400과 900을 만드는 경우
                elif s[idx] == 'C' and s[idx + 1] == 'D':
                    answer += 400
                    idx += 1
                elif s[idx] == 'C' and s[idx + 1] == 'M':
                    answer += 900
                    idx += 1
                else:
                    answer += symbol[s[idx]]
            else:
                answer += symbol[s[idx]]
            
            idx += 1
        
        return answer

s = Solution()
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))