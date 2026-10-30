class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for n in strs:
            keySorted = "".join(sorted(n))
            if keySorted in groups:
                groups[keySorted].append(n)
            else:
                groups[keySorted] = [n]
        return list(groups.values())