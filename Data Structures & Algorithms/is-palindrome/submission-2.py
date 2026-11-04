class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ""
        for i in range(len(s)):
            if s[i].isalnum():
                result += s[i]
        return result == result[::-1]