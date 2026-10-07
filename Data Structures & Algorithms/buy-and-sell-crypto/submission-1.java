class Solution {
    public int maxProfit(int[] prices) {
        int maxp = 0;
        for (int i = 0; i <= prices.length; i++){
            for(int j = i+1; j <= prices.length-1; j++){
                if(prices[j] - prices[i] > maxp){
                    maxp = prices[j] - prices[i];
                }
            }
        }
        return maxp;
    }
}

/* [10,1,5,6,7,1] 

*/