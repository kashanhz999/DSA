class Solution {
    public int[] runningSum(int[] nums) {
        int sz = nums.length;
        int sum = 0;
        int[] out = new int[sz];
        for(int i = 0;i<nums.length;i++){
            sum += nums[i];
            out[i] = sum;
        }
        return out;
    }
}