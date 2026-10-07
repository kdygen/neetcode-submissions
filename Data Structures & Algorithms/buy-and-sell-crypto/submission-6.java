class Solution {
    public int maxProfit(int[] prices) {
        int maxp = 0;
        int lowest = 10000000;
        for(int i = 0; i < prices.length; i++){
            if(prices[i] < lowest){
                lowest = prices[i];
            }
            if(prices[i] - lowest > maxp){
                maxp = prices[i] - lowest;
            }
        }
        return maxp;
    }
}

/* [10,1,5,6,7,1] 

*/