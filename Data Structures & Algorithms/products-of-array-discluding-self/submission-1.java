class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;      
        int[] result = new int[n];  

        for(int i = 0; i < nums.length; i++){
            int product = 1;
            for(int j = 0; j < nums.length; j++){
                if(i == j) continue;
                product *= nums[j];
            }
            result[i] = product;
        }
        return result;
    }
}  
