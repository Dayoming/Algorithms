class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        # 부호 저장
        sign = ''
        
        # 음수이면
        if x < 0:
            temp = str(x * -1)[::-1]
            sign = '-'
        # 0이면 0을 반환하고 종료
        elif x == 0:
            return 0
        # 양수이면
        else:    
            temp = str(x)[::-1]
            sign = ''
        
        idx = 0
        if temp[0] == '0':
            while temp[idx] == '0':
                idx += 1
                
        answer = int(sign + temp[idx::])
                
        # 뒤집었을 때 -2의 31승보다 크고 2의 31승 - 1보다 작으면
        if answer <= -(2 ** 31) or answer >= 2 ** 31 - 1:
            answer = 0
            
        return answer        

s = Solution()
print(s.reverse(1534236469))
# print(s.reverse(120))
# print(s.reverse(-123))
# print(s.reverse(123))