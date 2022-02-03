class Solution {
    public int[] countBits(int num) {
        
        if (num==0) return new int[1];
        
        int[] result = new int[num+1];
        result[1] = 1;
        for(int i=2;i<=num;i++){
            result[i] = result[i/2] + (i%2==0?0:1);
            
        }
        return result;
        
    }
}