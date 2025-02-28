class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;  // Avoids integer overflow
            
            if (nums[mid] == target) {
                return mid;  // Target found, return index
            } else if (nums[mid] < target) {
                left = mid + 1;  // Move right
            } else {
                right = mid - 1; // Move left
            }
        }
        
        return left;  // Left points to the insertion position
    }
}