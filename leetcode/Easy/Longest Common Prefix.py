class Solution:
    def longestCommonPrefix(self, strs):
        # 예외 처리: 빈 배열이나 빈 문자열이 입력되었을 경우
        if not strs or len(strs[0]) == 0:
            return ""
        
        # 첫 번째 문자열을 기준으로 설정
        prefix = strs[0]
        
        # 각 문자열과 비교하면서 prefix를 갱신
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                # prefix가 현재 문자열의 접두사가 아니라면 한 문자씩 줄여나감
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
                
        return prefix

s = Solution()
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(s.longestCommonPrefix(strs = ["dog","racecar","car"]))