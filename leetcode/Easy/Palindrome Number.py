class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return 'true'
        else:
            return 'false'

s = Solution()
print(s.isPalindrome(-121))
print(s.isPalindrome(121))
print(s.isPalindrome(10))