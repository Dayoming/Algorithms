class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 그냥 문자열이 팰린드롬이면 바로 return
        if s == s[::-1]:
            return s
        
        answer = []
        # 팰린드롬인 모든 경우의 수 저장
        for i in range(len(s) + 1):
            for j in range(i):
                temp = (s[j:i])
                if temp == temp[::-1]:
                    answer.append(temp)
        
        # 길이순으로 정렬
        answer.sort(key=len)
        
        # 가장 긴 팰린드롬 출력
        return answer[-1]

s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))