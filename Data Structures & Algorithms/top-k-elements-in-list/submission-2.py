class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        list1 = []
        for n in nums:
            if n in dict1:
                dict1[n] +=1
            else:
                dict1[n] = 1
        sortedDict = sorted(dict1.items(), key=lambda x: x[1], reverse = True)
        for i in range(k):
            list1.append(sortedDict[i][0])
        
        return list1