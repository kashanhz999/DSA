class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] r_sum = new int[n];
        int[] l_sum = new int[n];
        int[] out = new int[n];
        
        l_sum[0] =1;
        r_sum[n-1] = 1;
        
        for(int i=1;i<n;i++){
            l_sum[i] = nums[i-1] * l_sum[i-1];
        }
        for(int i=n-2;i>=0;i--){
            r_sum[i] = nums[i+1] * r_sum[i+1];
        }
        for(int i=0;i<n;i++){
            out[i] = l_sum[i] * r_sum[i];
        }
        
        return out;
    }
}