class Solution {
    public int findClosestNumber(int[] nums) {
        int ans=Integer.MAX_VALUE;
        
        for(int i=0;i<nums.length;i++){
            if(nums[i]>=0 && nums[i]<=Math.abs(ans))
                ans=nums[i];
            
        if(nums[i]<0 && Math.abs(nums[i]-0)<Math.abs(ans)){
            ans=nums[i];
        }
        }
        return ans;
    }
}