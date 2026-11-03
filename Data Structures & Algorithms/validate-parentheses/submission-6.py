class Solution:
    def isValid(self, s: str) -> bool:
        result = False 
        dict1 = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in range(len(s)):
            if s[i] in dict1.keys():
                stack.append(s[i])
            elif stack and s[i] == dict1[stack[-1]]:            #"([{}])"
                stack.pop()
            else:
                return False
        if stack == []:
            result = True

        return result
