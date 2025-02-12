class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n = nums.length;
        int[][] newNums = new int[n][2];
        for (int i = 0; i < n; i++) {
            newNums[i] = new int[] {nums[i], i};
        }
        Arrays.sort(newNums, (a, b) -> a[0] - b[0]);
        int[] res = new int[n];
        int j = 0;
        for (int i = 1; i < n; i++) {
            if (newNums[i][0] != newNums[i - 1][0]) {
                j = i;
            }
            res[newNums[i][1]] = j;
        }
        return res;
    }
}