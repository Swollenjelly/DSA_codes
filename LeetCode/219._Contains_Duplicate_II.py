class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer,Integer> lastSeen = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            if(lastSeen.containsKey(nums[i])){
                if(Math.abs(i-lastSeen.get(nums[i]))<=k){
                    return true;
                }
            }
            lastSeen.put(nums[i],i);
        }

        return false;
        
    }
}