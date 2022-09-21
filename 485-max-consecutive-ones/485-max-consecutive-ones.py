class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        maxC = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                c +=1
            else:
                c = 0
            maxC= max(c,maxC)
        return maxC
                
        