class Solution {
    public int maxProfit(int[] prices) {
        int r = 1, l = 0;
        int maxProf = 0;

       while(r<prices.length){
         if(prices[l]<prices[r]){
            int prof = prices[r] - prices[l];
            maxProf = Math.max(prof, maxProf);

            r+=1;
        }
        else{
            l = r;
            r+=1;
        }
        
       }
       return maxProf;
    }
    
}