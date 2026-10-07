
class Solution {

    public boolean hasDuplicate(int[] nums) {
        boolean isonce = false;
        for (int i = 0; i < nums.length; i++){
            for(int k = i+1; k < nums.length; k++){
                if(nums[k] == nums[i]){
                    isonce = true;
                }
            }
        }
        return isonce;
    }
}