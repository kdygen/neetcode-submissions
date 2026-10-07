class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for n in s:
            if n in dict1:
                dict1[n] +=1
            else:
                dict1[n] = 1
        for n in t:
            if n in dict2:
                dict2[n] +=1
            else:
                dict2[n] = 1
        if dict1 == (dict2):
            return True
        return False