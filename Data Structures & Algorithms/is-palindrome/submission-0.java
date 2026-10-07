class Solution {
    public boolean isPalindrome(String s) {
        String newS = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        String reversed = new StringBuilder(newS).reverse().toString();
        return newS.equals(reversed);
    }
}
