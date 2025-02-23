class Solution {
    public int longestMountain(int[] arr) {

        if(arr.length <3){
            return 0;
        }
        int maxLength = 0;

        for(int i=1; i<arr.length-1; i++){

            if(arr[i]>arr[i-1] && arr[i]> arr[i+1]){
                int left = i;
                int right = i;

                while(left>0 && arr[left]>arr[left-1]){
                    left--;
                }

                while(right< arr.length-1 && arr[right]>arr[right+1]){
                    right++;
                }

                int mountainLength = right - left + 1;
                maxLength =Math.max(mountainLength, maxLength); 

                i = right;
            }

            
        }

        return maxLength;
        
        
    }
}
