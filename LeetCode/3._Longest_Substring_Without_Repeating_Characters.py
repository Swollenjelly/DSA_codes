class Solution {
    public int lengthOfLongestSubstring(String s) {
       HashMap<Character,Integer> charMap = new HashMap<>();
       int left=0;
       int maxlen=0;
       int right=0;

       for(right=0; right<s.length(); right++){
        if(charMap.containsKey(s.charAt(right)) && charMap.get(s.charAt(right))>=left){
            left=charMap.get(s.charAt(right))+1;
            }

            charMap.put(s.charAt(right),right);
            maxlen=Math.max(maxlen, right-left+1);
       }
       return maxlen;
}
}