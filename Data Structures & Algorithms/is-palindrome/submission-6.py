class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ""
        isTrue = True
        for i in range(len(s)):
            if s[i].isalnum() == True:
                result += s[i]
        for i in range(len(result)//2):
            if result[i] == result[-(i+1)]:     # 0 -1; 1 -2; 2 -3
                isTrue = True
            else:
                isTrue = False
                break
        return isTrue