class Solution {
    public int maxProfit(int[] prices) {
        int buy = 0;
        int maxProfit = 0;
        for (int i = 1; i<prices.length; i++){
           if (prices[i] - prices[buy] > maxProfit){
            maxProfit = prices[i] - prices[buy];
           }
           else if(prices[i]<prices[buy]){
                buy = i;
           }
        }
        return maxProfit;
    }
}
