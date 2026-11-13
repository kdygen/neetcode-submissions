class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            newStone = -abs(stone1 - stone2)
            if newStone != 0:
                heapq.heappush(heap, newStone)
            

        if heap:
            return -heap[0]

        return 0         