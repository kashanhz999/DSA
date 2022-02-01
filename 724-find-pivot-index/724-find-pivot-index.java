class Solution {
    public int pivotIndex(int[] nums) {
        int sz = nums.length;
        int sum =0;
        for(int i=0;i<sz;i++){
            sum+= nums[i];
        }
        int leftsum = 0;
        int rightsum = 0;
        
        for(int i = 0;i<sz;i++){
            rightsum = sum-leftsum-nums[i];
            if(leftsum == rightsum){
                return i;
            }
            leftsum += nums[i];
        }
        return -1;
    }
}