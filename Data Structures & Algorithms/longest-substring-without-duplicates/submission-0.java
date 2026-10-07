class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> seen = new HashMap<>();
        int left = 0;
        int maxlen = 0;

        for( int right = 0; right < s.length(); right++){
            char c = s.charAt(right);

            if(seen.containsKey(c) && seen.get(c) >= left){
                left = seen.get(c) + 1;
            }

            seen.put(c, right);
            maxlen = Math.max(maxlen, right - left +1);
        }
        return maxlen;
    }
}
