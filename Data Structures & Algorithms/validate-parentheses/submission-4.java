class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<>();
        Map<String, String> brackets = Map.of( 
            "{", "}",
            "[", "]",
            "(", ")"
            );
        for (int i = 0; i < s.length(); i++){
            String current = String.valueOf(s.charAt(i));
            if (brackets.containsKey(current)){
                stack.push(current);
            }
            else{
            if(stack.isEmpty()){
                return false;
            }
            String top = stack.pop();
            String expectedClosing = brackets.get(top);
            if(!current.equals(expectedClosing)){
                return false;
            }
            }
        }
        return stack.isEmpty();
    }
}