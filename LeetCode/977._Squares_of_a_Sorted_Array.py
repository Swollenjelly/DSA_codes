class Solution {
    public int[] sortedSquares(int[] nums) {

        int sqNums[] = new int[nums.length];

        for(int i = 0; i < nums.length; i++){
            sqNums[i] = nums[i]*nums[i];
        }

        Arrays.sort(sqNums);
        return sqNums;
        
    }
}