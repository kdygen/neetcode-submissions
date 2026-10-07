
class Solution {

    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        int k = 0;
        boolean isonce = false;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[k]){
                k++;
            } else {
                isonce = true;
            }
        }
        return isonce;
    }
}