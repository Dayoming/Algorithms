class Solution:
    def isValid(self, s: str) -> bool:
        answer = False
        stack = []
        open_bracket = ['(', '[', '{']
        
        for c in s:
            # 만약 여는 괄호가 들어오면 무조건 넣어준다
            if c in open_bracket:
                stack.append(c)
            # 닫는 괄호가 들어오는 경우
            else:
                # stack이 비어있거나, 리스트의 마지막 요소가 해당하는 여는 괄호가 아니라면 False를 return
                if not stack or (stack[-1] == '(' and c != ')') or (stack[-1] == '[' and c != ']') or (stack[-1] == '{' and c != '}'):
                    return False
                else:
                    del stack[-1]
        
        if stack:
            answer = False
        else:
            answer = True
        
        return answer

s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("()(]"))