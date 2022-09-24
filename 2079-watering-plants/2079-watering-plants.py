class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        curCap = capacity
        n = len(plants)
        steps = 0
        
        for i in range(n):
            #refill 
            if plants[i] > curCap:
                curCap = capacity 
                steps += 2*i+1
            else:
                steps+=1
            curCap = curCap - plants[i]
            
        return steps
                
        