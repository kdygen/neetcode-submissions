class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit  = 0
        left = 0 
        right = 1      #[10,1,5,6,7,1]
        while right < len(prices):
            if prices[right]<prices[left]:
                left = right
            elif prices[right] - prices[left] > profit:   
                profit = prices[right] - prices[left]
            right += 1
        return profit