class Solution {
    public boolean isPalindrome(String s) {
        String clean = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String s2 = new StringBuilder(clean).reverse().toString();
        return clean.equals(s2);
    }
}