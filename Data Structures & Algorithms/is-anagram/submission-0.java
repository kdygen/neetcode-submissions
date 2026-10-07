class Solution {
    public boolean isAnagram(String s, String t) {
        char[] chars1 = s.toCharArray();
        Arrays.sort(chars1);
        char[] chars2 = t.toCharArray();
        Arrays.sort(chars2);

        String newStr1 = new String(chars1);
        String newStr2 = new String(chars2);

        if(newStr1.equals(newStr2)){
            return true;
        } else{
            return false;
        }
    }
}
