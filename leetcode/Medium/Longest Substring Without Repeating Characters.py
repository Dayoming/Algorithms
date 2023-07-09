class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = 0
        answer = 0
        # 전체 문자열에서 검사한 문자열 수 만큼 제외한 부분 검사
        for i in range(temp, len(s) - temp):
            p = s[temp:i + 1]
            # 중복을 제거한 문자열과 같으면 - 부분 문자열이 중복되지 않으면
            if(len(p) == len(set(p))):
                # 문자열 최대값 갱신
                answer = max(len(p), answer)
            else:
                temp += 1
        return answer

s = Solution()
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))