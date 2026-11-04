class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        a = s[0]
        right = 1
        count = 1
        longest = 1
        #a[0] != s[right]
        while right < len(s):       #abc - b - cb
            while s[right] in a:
                a = a[1:]
                count -=1
            a += s[right]
            right += 1 
            count +=1
            if count > longest:
                longest = count
        return longest