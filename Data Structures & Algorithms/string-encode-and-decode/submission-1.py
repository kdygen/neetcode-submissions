class Solution:

    def encode(self, strs: List[str]) -> str:
        count = 0
        a = ""
        for n in strs:
            count = len(n)
            a += f"{count},{n}" 
        return a 
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = i

        while i < len(s):
            while s[j] != ",":
                j += 1
            count = int(s[i: j])
            result.append(s[j+1:j+1+count])
            i = count + 1 + j
            j = i
        return result
